import copy
import sys
import time

import src.sexp as sexp
import util.translator as translator
from train import train
from util.filter import global_filter
from util.parsing import ParseSynFunc, StripComments
from util.priority_queue import Priority_Queue, Select
from util.cut_branch import Abstract
from util.prob import *
import logging

logging.basicConfig(filename='main.log', filemode='w', level='INFO')


def extend_with_prob(statements_now, statements_top, check_branch, dis_top, productions_with_prob, prob_upperbounds, params,
                     queue_dis, queue):
    ret = []
    updated = False

    for i in range(len(statements_now)):
        #print(statements_now[i])
        # Recursively search the non-terminals, e.g. [* Start Start]
        if type(statements_now[i]) is list:
            updated = updated or extend_with_prob(statements_now[i], statements_top, check_branch, dis_top, productions_with_prob,
                                                  prob_upperbounds, params, queue_dis, queue)

        elif type(statements_now[i]) is tuple:
            continue

        elif statements_now[i] in productions_with_prob:
            updated = True

            if i == 0:
                context = ('{root}', '{empty}')
            else:
                context = (feature_transform(statements_now[0], params),
                           '{empty}' if i == 1 else feature_transform(statements_now[i - 1], params))

            prev = statements_now[i]
            for extended, prob in productions_with_prob[prev][context]:
                statements_now[i] = extended
                next_statement = statements_top

                dis = dis_top + prob_to_dis(prob)

                if global_filter(next_statement) and check_branch(next_statement):
                    next_str = str(next_statement)
                    if next_str not in queue_dis:
                        queue_dis[next_str] = dis
                        queue.add_item(copy.deepcopy(next_statement),
                                       dis + get_statements_heuristics(next_statement, prob_upperbounds))
                    elif queue_dis[next_str] > dis:
                        queue_dis[next_str] = dis

                statements_now[i] = prev  # recover

    return updated


def extend(statements, check_branch, dis, productions_with_prob, prob_upperbounds, params, visit, queue):
    return extend_with_prob(statements, statements, check_branch, dis, productions_with_prob, prob_upperbounds, params, visit, queue)


def Search(Checker, Check_branch, FuncDefine, productions_with_prob, prob_upperbounds, params, StartSym):
    Ans = None  # set of searched expression
    BfsQueue = Priority_Queue()  # search queue
    FuncDefineStr = translator.toString(FuncDefine, ForceBracket=True)

    queue_dis = {str([StartSym]): 0}

    BfsQueue.add_item([StartSym])
    extend_time, check_time = 0, 0
    select_time = 0
    loop_count = 0

    # Top-down search
    while len(BfsQueue) != 0:
        loop_count += 1

        start_select_time = time.time()
        Curr = Select(BfsQueue)  # ((Statement, dis), cost)
        curr_str = str(Curr)
        dis = queue_dis[curr_str]

        end_select_time = time.time()
        select_time += end_select_time - start_select_time

        if loop_count % 10000 == 0:
            print(f"{loop_count}: {Curr}")
            print(f"Select: {select_time}")
            print(f"Extend: {extend_time}\nCheck: {check_time}")
            print('\n\n')
        start_extend_time = time.time()
        extend_res = extend(Curr, Check_branch, dis, productions_with_prob, prob_upperbounds, params, queue_dis, BfsQueue)
        end_extend_time = time.time()
        extend_time += end_extend_time - start_extend_time

        # Nothing to extend, check correctness
        start_check_time = time.time()
        if not extend_res:  # not updated
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

    print(f"Select: {select_time}")
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

    StartSym = 'My-Start-Symbol'  # start symbol
    FuncDefine = ['define-fun'] + SynFunExpr[1:4]  # copy function signature
    Type, Productions, isIte = ParseSynFunc(SynFunExpr, StartSym)
    check_branch = Abstract(Logic, FuncCallList, SynFunExpr, Productions, Type)

    params = set([param[0] for param in SynFunExpr[2]])
    train_data = open('training_data.sl')
    statistics = train(train_data)
    productions_with_prob, prob_upperbounds = (
        get_production_prob(params, Productions, statistics, StartSym))

    Ans = Search(checker, check_branch, FuncDefine, productions_with_prob, prob_upperbounds, params, StartSym)

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
