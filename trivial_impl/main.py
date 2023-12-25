import sys, os, time
import src.sexp as sexp
import util.translator as translator
from util.parsing import ParseSynFunc, StripComments
from util.priority_queue import Priority_Queue, Select
from util.filter import global_filter
# from mysolver import hasIte, getSynFunExpr, Solver
from util.hint import Hint


def Extend(Stmts, Productions, Types, hint):
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
    ret_now = []

    for i in range(len(Stmts)):
        # Recursively search the non-terminals, e.g. [* Start Start]
        if type(Stmts[i]) is list:
            TryExtend, _ = Extend(Stmts[i], Productions, Types, hint)
            if len(TryExtend) > 0:
                ret.extend(Stmts[0:i] + [extended] + Stmts[i+1:]
                           for extended in TryExtend
                           if global_filter(Stmts[0:i] + [extended] + Stmts[i+1:]))
        elif type(Stmts[i]) is tuple:
            continue
        else:
            if Stmts[i] in Types.keys() and Types[Stmts[i]] == 'Int':
                new_list = hint.gen_stmt_from_hint()
                if new_list is not None and len(new_list) > 0:
                    ret_now.append(Stmts[0:i] + new_list + Stmts[i + 1:])
            # Unfold the non-terminals
            if Stmts[i] in Productions:
                ret.extend(Stmts[0:i] + [extended] + Stmts[i+1:]
                           for extended in Productions[Stmts[i]]
                           if global_filter(Stmts[0:i] + [extended] + Stmts[i+1:]))
    return ret, ret_now


def Search(Checker, FuncDefine, Type, Productions, hint, StartSym='My-Start-Symbol'):
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
    TE_memory = set()                              # set of searched expression
    BfsQueue = Priority_Queue(Productions.keys())  # search queue
    Ans = None                                     # answer of the program
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
        TryExtend, TryNow = Extend(Curr, Productions, Type, hint)
        print(TryNow)
        end_extend_time = time.time()
        extend_time += end_extend_time - start_extend_time

        for check_stmt in TryNow:
            CurrStr = translator.toString(check_stmt)
            Str = FuncDefineStr[:-1] + ' ' + CurrStr + FuncDefineStr[-1]
            counterexample = Checker.check(Str)
            if counterexample is None:  # No counter-example
                print(f'find answer in loop {loop_count}')
                Ans = Str
                break
        if Ans is not None:
            break

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
    StartSynthesis = time.time()
    # Parsing file to expression list
    bm = StripComments(benchmarkFile)
    bmExpr = sexp.sexp.parseString(bm, parseAll=True).asList()[0]
    checker, hint = translator.ReadQuery(bmExpr)
    SynFunExpr = []

    for expr in bmExpr:
        if len(expr) > 0 and expr[0] == 'synth-fun':
            SynFunExpr = expr
            break

    StartSym = 'My-Start-Symbol'                   # start symbol
    FuncDefine = ['define-fun'] + SynFunExpr[1:4]  # copy function signature
    Type, Productions, isIte = ParseSynFunc(SynFunExpr, StartSym)

    StartSearch = time.time()
    Ans = Search(checker, FuncDefine, Type, Productions, hint, StartSym)
    EndSearch = time.time()
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
