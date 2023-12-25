import sys
import time

import src.sexp as sexp
import util.translator as translator
from train import train
from util.filter import global_filter
from util.parsing import ParseSynFunc, StripComments
from util.priority_queue import Priority_Queue, Select
from util.prob import *


logging.basicConfig(filename='main.log', filemode='w', level='INFO')


def extend_with_prob(statements_now, statements_top, dis_top, productions_with_prob, params):
    ret = []
    for i in range(len(statements_now)):
        # Recursively search the non-terminals, e.g. [* Start Start]
        if type(statements_now[i]) is list:
            TryExtend = extend_with_prob(statements_now[i],
                                         statements_top,
                                         dis_top,
                                         productions_with_prob,
                                         params)

            for extended, dis in TryExtend:
                next_statement = statements_now[0:i] + [extended] + statements_now[i + 1:]
                if global_filter(next_statement):
                    ret.append((next_statement, dis))

        elif type(statements_now[i]) is tuple:
            continue

        elif statements_now[i] in productions_with_prob:
            if i == 0:
                context = ('{root}', '{empty}')
            else:
                context = (feature_transform(statements_now[0], params),
                           '{empty}' if i == 1 else feature_transform(statements_now[i - 1], params))
            for extended, prob in productions_with_prob[statements_now[i]][context]:
                next_statement = statements_now[0:i] + [extended] + statements_now[i + 1:]
                if global_filter(next_statement):
                    ret.append((next_statement, dis_top + prob_to_dis(prob)))

    return ret


def extend(statements, dis, productions_with_prob, params):
    return extend_with_prob(statements, statements, dis, productions_with_prob, params)


def Search(Checker, FuncDefine, productions_with_prob, prob_upperbounds, params, StartSym):
    Ans = None  # set of searched expression
    BfsQueue = Priority_Queue(productions_with_prob.keys())  # search queue
    FuncDefineStr = translator.toString(FuncDefine, ForceBracket=True)

    BfsQueue.add_item(([StartSym], 0))
    update_time = 0
    extend_time, check_time = 0, 0
    select_time = 0
    loop_count = 0

    # Top-down search
    while len(BfsQueue) != 0:
        loop_count += 1

        start_select_time = time.time()
        Curr = Select(BfsQueue)  # ((Statement, dis), cost)
        Curr, dis = Curr[0], Curr[1]

        logging.info(f'curr cost is {dis + get_statements_heuristics(Curr, prob_upperbounds)}')

        end_select_time = time.time()
        select_time += end_select_time - start_select_time

        if loop_count % 10000 == 0:
            print(f"{loop_count}: {Curr}")
            print(f"Select: {select_time}")
            print(f"Update: {update_time}")
            print(f"Extend: {extend_time}\nCheck: {check_time}")
            print('\n\n')
        start_extend_time = time.time()
        TryExtend = extend(Curr, dis, productions_with_prob, params)
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
        for statement, dis in TryExtend:
            cost = dis + get_statements_heuristics(statement, prob_upperbounds)
            BfsQueue.add_item((statement, dis), cost)
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
            get_production_prob(params, Productions, statistics, StartSym))

    Ans = Search(checker, FuncDefine, productions_with_prob, prob_upperbounds, params, StartSym)

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
