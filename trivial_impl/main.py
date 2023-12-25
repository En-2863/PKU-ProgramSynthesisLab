import sys, os, time
import src.sexp as sexp
import util.translator as translator
from util.parsing import ParseSynFunc, StripComments
from util.priority_queue import Priority_Queue, Select
from train import train

from util.filter import global_filter
from util.prob import *


def Extend(Stmts, Productions, Types):
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

    for i in range(len(Stmts)):
        # Recursively search the non-terminals, e.g. [* Start Start]
        if type(Stmts[i]) is list:
            TryExtend = Extend(Stmts[i], Productions, Types)
            if len(TryExtend) > 0:
                ret.extend(Stmts[0:i] + [extended] + Stmts[i + 1:]
                           for extended in TryExtend
                           if global_filter(Stmts[0:i] + [extended] + Stmts[i + 1:]))
        elif type(Stmts[i]) is tuple:
            continue
        elif Stmts[i] in Productions:
            ret.extend(Stmts[0:i] + [extended] + Stmts[i + 1:]
                       for extended in Productions[Stmts[i]]
                       if global_filter(Stmts[0:i] + [extended] + Stmts[i + 1:]))
    return ret


def extend_with_prob(statements_now, statements_top, dis_top, seq, productions_with_prob, params):
    assert get_seq(statements_top, seq) == statements_now

    ret = []
    for i in range(len(statements_now)):
        # Recursively search the non-terminals, e.g. [* Start Start]
        if type(statements_now[i]) is list:
            seq.append(i)
            TryExtend = extend_with_prob(statements_now[i], statements_top, dis_top, seq, productions_with_prob, params)
            seq.pop(-1)

            if len(TryExtend) > 0:
                ret.extend((statements_now[0:i] + [extended] + statements_now[i + 1:], dis)
                           for (extended, dis) in TryExtend
                           if global_filter(statements_now[0:i] + [extended] + statements_now[i + 1:]))
        elif type(statements_now[i]) is tuple:
            continue
        elif statements_now[i] in productions_with_prob:
            context = get_transformed_context(statements_top, seq, params)
            ret.extend((statements_now[0:i] + [extended] + statements_now[i + 1:], dis_top + prob_to_dis(prob))
                       for (extended, prob) in productions_with_prob[statements_now[i]][context]
                       if global_filter(statements_now[0:i] + [extended] + statements_now[i + 1:]))
    return ret


def extend_with_heuristic(statements, dis, productions_with_prob, params, prob_upperbounds):
    try_extend = extend_with_prob(statements, statements, dis, [], productions_with_prob, params)
    for i in range(len(try_extend)):
        try_extend[1] += get_statements_heuristics(try_extend[0], prob_upperbounds)
    return try_extend


def Search(Checker, FuncDefine, Type, Productions, StartSym='My-Start-Symbol'):
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
    Ans = None                                       # set of searched expression
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
        Curr, length = Curr[0], Curr[1]
        end_select_time = time.time()
        select_time += end_select_time - start_select_time

        if loop_count % 10000 == 0:
            print(f"{loop_count}: {Curr}")
            print(f"Select: {select_time}")
            print(f"Update: {update_time}")
            print(f"Extend: {extend_time}\nCheck: {check_time}")
            print('\n\n')
        start_extend_time = time.time()
        TryExtend = Extend(Curr, Productions, Type)
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
            BfsQueue.add_item(TE, 0)
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
    checker = translator.ReadQuery(bmExpr)
    SynFunExpr = []

    for expr in bmExpr:
        if len(expr) > 0 and expr[0] == 'synth-fun':
            SynFunExpr = expr
            break

    StartSym = 'My-Start-Symbol'  # start symbol
    FuncDefine = ['define-fun'] + SynFunExpr[1:4]  # copy function signature
    Type, Productions, isIte = ParseSynFunc(SynFunExpr, StartSym)

    productions_with_prob = None
    prob_upperbounds = None
    params = set([param[0] for param in SynFunExpr[2]])

    if len(sys.argv) > 2:
        train_data = open(sys.argv[2])
        statistics = train(train_data)
        productions_with_prob, prob_upperbounds = (
            get_production_prob(params, Productions, statistics, 'Start'))

    Ans = Search(checker, FuncDefine, Type, Productions, StartSym)

    print(Ans)

    with open('result.txt', 'w') as f:
        f.write(Ans)


if __name__ == '__main__':
    benchmarkFile = open(sys.argv[1])
    ProgramSynthesis(benchmarkFile)

    # Examples of counter-examples
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int 0)'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int x)'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int (+ x y))'))
