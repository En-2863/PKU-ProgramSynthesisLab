import sys, os, time
import src.sexp as sexp
import util.translator as translator
from util.parsing import ParseSynFunc, StripComments
from util.priority_queue import Priority_Queue, Select
from util.filter import global_filter
from util.prob import *
from util.cut_branch import Abstract
from train import train


def Extend(Stmts, Productions, Types, check_branch):
    """
    Given a statement and replace the non-terminals
    according to rules from productions.

    Args:
        Stmts (List(Symbol)):
            A list representing a statement, e.g. [[* Start Start]]
        Productions (Dict(Symbol: List(Symbol) )):
            Rules from synth-fun.

    Returns:
        List(Statements): Extended statements from the origin.
    """
    ret = []
    #stmts = [['ite', 'StartBool', 'Start', 'Start']]
    #print(check_branch(stmts))

    for i in range(len(Stmts)):
        # Recursively search the non-terminals, e.g. [* Start Start]
        if type(Stmts[i]) is list:
            TryExtend = Extend(Stmts[i], Productions, Types, check_branch)
            if len(TryExtend) > 0:
                ret.extend(Stmts[0:i] + [extended] + Stmts[i+1:]
                           for extended in TryExtend
                           if global_filter(Stmts[0:i] + [extended] + Stmts[i+1:]))
                           #and check_branch(Stmts[0:i] + [extended] + Stmts[i+1:]))
        elif type(Stmts[i]) is tuple:
            continue
        elif Stmts[i] in Productions:
            ret.extend(Stmts[0:i] + [extended] + Stmts[i+1:]
                       for extended in Productions[Stmts[i]]
                       if global_filter(Stmts[0:i] + [extended] + Stmts[i+1:]))
                       #and check_branch(Stmts[0:i] + [extended] + Stmts[i+1:]))
    return ret


def Search(Checker, check_branch, FuncDefine, Type, Productions, StartSym='My-Start-Symbol'):
    """Search programs that satisfies predefined functions.
        WARNING: THIS FUNCTION WILL LOOP UNTIL ANSWER IS REACHED.

    Args:
        Checker (Checker):
            A checker based on z3 solver.
        FuncDefine (List(Symbols)):
            A list of symbols defines the function.
        Type (Dict(Symbol: Type)):
            Return type of symbols
        Productions (Dict(Symbol: List(Expressions))):
            Production rules for given symbols
        StartSym (str, optional):
            Defaults to 'My-Start-Symbol'.

    Returns:
        Expression: Answer to the benchmark.
    """
    Ans = None                                     # answer of the program
    TE_memory = set()                              # set of searched expression
    BfsQueue = Priority_Queue(Productions.keys())  # search queue
    FuncDefineStr = translator.toString(FuncDefine, ForceBracket=True)

    BfsQueue.add_item([StartSym])
    update_time = 0
    extend_time, check_time = 0, 0
    select_time = 0
    loop_count = 0

    # Top-down search
    while len(BfsQueue) != 0:
        loop_count += 1

        start_select_time = time.time()
        Curr = Select(BfsQueue)
        end_select_time = time.time()
        select_time += end_select_time - start_select_time

        if loop_count % 10000 == 0:
            print(f"{loop_count}: {Curr}")
            print(f"Select: {select_time}")
            print(f"Update: {update_time}")
            print(f"Extend: {extend_time}\nCheck: {check_time}")
            print('\n\n')
        start_extend_time = time.time()
        TryExtend_Pre = Extend(Curr, Productions, Type, check_branch)
        TryExtend = []
        for extend_stmt in TryExtend_Pre:
            #print(f"check {extend_stmt}:")
            if check_branch(extend_stmt) is True:
                TryExtend.append(extend_stmt)
                #print(f"check ok {extend_stmt}")
            #print("\n")
        #print("\n\n")
        end_extend_time = time.time()
        extend_time += end_extend_time - start_extend_time

        # Nothing to extend, check correctness
        start_check_time = time.time()
        if len(TryExtend) == 0:
            # Insert Program just before the last bracket ')'
            CurrStr = translator.toString(Curr)
            Str = FuncDefineStr[:-1] + ' ' + CurrStr + FuncDefineStr[-1]
            counterexample = Checker.check(Str)

            # No counter-example
            if counterexample is None:
                print(f'find answer in loop {loop_count}')
                Ans = Str
                end_check_time = time.time()
                check_time += end_check_time - start_check_time
                break
        end_check_time = time.time()
        check_time += end_check_time - start_check_time

        start_update_time = time.time()
        for TE in TryExtend:
            TE_str = str(TE)
            if TE_str not in TE_memory:
                BfsQueue.add_item(TE)
                TE_memory.add(TE_str)
        end_update_time = time.time()
        update_time += end_update_time - start_update_time

    print(f"Select: {select_time}")
    print(f"Update: {update_time}")
    print(f"Extend: {extend_time}\nCheck: {check_time}")
    return Ans


def ProgramSynthesis(benchmarkFile):
    # StartSynthesis = time.time()
    # Parsing file to expression list
    bm = StripComments(benchmarkFile)
    bmExpr = sexp.sexp.parseString(bm, parseAll=True).asList()[0]
    checker, Logic, FuncCallList, SynFunExpr = translator.ReadQuery(bmExpr)
    SynFunExpr = []

    for expr in bmExpr:
        if len(expr) > 0 and expr[0] == 'synth-fun':
            SynFunExpr = expr
            break

    StartSym = 'My-Start-Symbol'                   # start symbol
    FuncDefine = ['define-fun'] + SynFunExpr[1:4]  # copy function signature
    Type, Productions, isIte = ParseSynFunc(SynFunExpr, StartSym)
    check_branch = Abstract(Logic, FuncCallList, SynFunExpr, Productions, Type)


    if len(sys.argv) > 2:
        trainData = open(sys.argv[2])
        statistics = train(trainData)
        get_production_prob(set([param[0] for param in SynFunExpr[2]]), Productions, statistics, 'Start')

    # StartSearch=time.time()
    Ans = Search(checker, check_branch, FuncDefine, Type, Productions, StartSym)
    # else:
    #    Ans = Solver(bmExpr)
    # EndSearch = time.time()
    print(Ans)

    with open('result.txt', 'w') as f:
        f.write(Ans)
        # f.write("\nSynthesis time: %f\nSearch time: %f"%((EndSearch-StartSynthesis),(EndSearch-StartSearch)))


if __name__ == '__main__':

    benchmarkFile = open(sys.argv[1])
    ProgramSynthesis(benchmarkFile)

    # Examples of counter-examples
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int 0)'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int x)'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int (+ x y))'))
