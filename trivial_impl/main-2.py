import sys, os, time
import src.sexp as sexp
import util.translator as translator
import multiprocessing
from util.parsing import ParseSynFunc, StripComments
from util.priority_queue import Priority_Queue, Select
from util.counterexample import UpdateSearchSpace
from util.filter import global_filter
from functools import partial


def Extend(Stmts, Productions):
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
            TryExtend = Extend(Stmts[i], Productions)
            if len(TryExtend) > 0:
                ret.extend(Stmts[0:i] + [extended] + Stmts[i+1:]
                           for extended in TryExtend
                           if global_filter(Stmts[0:i] + [extended] + Stmts[i+1:]))
        # Terminals
        elif type(Stmts[i]) is tuple:
            continue
        # Unfold the non-terminals
        elif Stmts[i] in Productions:
            ret.extend(Stmts[0:i] + [extended] + Stmts[i+1:]
                       for extended in Productions[Stmts[i]]
                       if global_filter(Stmts[0:i] + [extended] + Stmts[i+1:]))
    return ret


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
    TE_memory = set()                              # set of searched expression
    BfsQueue = Priority_Queue()                    # search queue
    Ans = None                                     # answer of the program

    BfsQueue.add_item([StartSym])

    loop_count = 0

    # Top-down search
    while len(BfsQueue) != 0:
        loop_count += 1

        Curr = Select(BfsQueue)
        TryExtend = Extend(Curr, Productions)

        # Nothing to extend, check correctness
        if len(TryExtend) == 0:
            # Use Force Bracket = True on function definition. MAGIC CODE.
            # DO NOT MODIFY THE ARGUMENT ForceBracket = True.
            FuncDefineStr = translator.toString(FuncDefine, ForceBracket=True)

            # Insert Program just before the last bracket ')'
            CurrStr = translator.toString(Curr)
            Str = FuncDefineStr[:-1] + ' ' + CurrStr + FuncDefineStr[-1]
            counterexample = Checker.check(Str)

            # No counter-example
            if counterexample is None:
                print(f'find answer in loop {loop_count}')
                Ans = Str
                break
            else:
                # TODO: counterexample-guided optimization
                UpdateSearchSpace(counterexample, BfsQueue)

        for TE in TryExtend:
            TE_str = str(TE)
            if TE_str not in TE_memory:
                BfsQueue.add_item(TE)
                TE_memory.add(TE_str)

    return Ans


def ParrallelExtend(bmExpr, FuncDefine, Type, Productions, Curr):
    # print(Curr)
    Curr = list(Curr)
    # print(Curr)
    start_extend_time = time.time()
    TryExtend = Extend(Curr, Productions)
    end_extend_time = time.time()
    extend_time = end_extend_time - start_extend_time
    # print(TryExtend)

    start_check_time = time.time()
    if len(TryExtend) == 0:
        
        Checker = translator.ReadQuery(bmExpr)
        FuncDefineStr = translator.toString(FuncDefine, ForceBracket=True)
        CurrStr = translator.toString(Curr)
        Str = FuncDefineStr[:-1] + ' ' + CurrStr + FuncDefineStr[-1]
        # print(Str)
        counterexample = Checker.check(Str)

        if counterexample is None:
            end_check_time = time.time()
            check_time = end_check_time - start_check_time
            return (True, Str, extend_time, check_time)
        # else:
            # TODO: counterexample-guided optimization
            # UpdateSearchSpace(counterexample, BfsQueue)
    end_check_time = time.time()
    check_time = end_check_time - start_check_time
    return (False, TryExtend, extend_time, check_time)


def ParrallelSearch(bmExpr, FuncDefine, Type, Productions, StartSym='My-Start-Symbol'):
    ParrallelExtendPartial = partial(ParrallelExtend, bmExpr,
                                     FuncDefine, Type, Productions)
    TE_memory = set()                              # set of searched expression
    BfsQueue = Priority_Queue()                    # search queue
    Ans = None                                     # answer of the program
    BfsQueue.add_item([StartSym])
    num_processes = 8
    create_time, select_time = 0, 0
    process_time, update_time = 0, 0
    extend_time, check_time = 0, 0
    iteration = 0
    p = 0

    with multiprocessing.Pool() as pool:
        while True:
            iteration += 1
            BfsQueueSize = len(BfsQueue.queue)
            async_results = []
            start_create_time = time.time()
            p += min(BfsQueueSize, num_processes)
            for i in range(min(BfsQueueSize, num_processes)):
                Curr = Select(BfsQueue)
                start_select_time = time.time()
                # print(f"here: {Curr}")
                end_select_time = time.time()
                select_time += end_select_time - start_select_time
                async_results.append(pool.apply_async(ParrallelExtendPartial,
                                                      args=[Curr]))
            end_create_time = time.time()
            create_time += end_create_time - start_create_time
            start_process_time = time.time()

            output_results = [result.get() for result in async_results]
            end_process_time = time.time()
            process_time += end_process_time - start_process_time

            start_update_time = time.time()

            for result in output_results:
                if result[0] is False:
                    TryExtend = result[1]
                    extend_time += result[2]
                    check_time += result[3]

                    for TE in TryExtend:
                        TE_str = str(TE)
                        if TE_str not in TE_memory:
                            BfsQueue.add_item(TE)
                            TE_memory.add(TE_str)
                else:
                    # print(result[1])
                    Ans = result[1]

            end_update_time = time.time()
            update_time += end_update_time - start_update_time
            if Ans is not None:
                break
        pool.close()
        pool.join()
    print(f"Create: {create_time}\nSelect: {select_time}")
    print(f"Process: {process_time}\nUpdate: {update_time}")
    print(f"Extend: {extend_time}\nCheck: {check_time}")
    print(f"Iteration: {iteration}\nProcess: {p}")
    print(f"Process/Iteration: {p / iteration}")
    return Ans


def ProgramSynthesis(benchmarkFile):
    StartSynthesis = time.time()
    # Parsing file to expression list
    bm = StripComments(benchmarkFile)
    bmExpr = sexp.sexp.parseString(bm, parseAll=True).asList()[0]
    checker = translator.ReadQuery(bmExpr)
    SynFunExpr = []

    for expr in bmExpr:
        if len(expr) > 0 and expr[0] == 'synth-fun':
            SynFunExpr = expr
            break

    StartSym = 'My-Start-Symbol'                   # start symbol
    FuncDefine = ['define-fun'] + SynFunExpr[1:4]  # copy function signature
    Type, Productions = ParseSynFunc(SynFunExpr, StartSym)
    # print(Productions)

    StartSearch = time.time()
    # Ans = Search(checker, FuncDefine, Type, Productions, StartSym)
    Ans = ParrallelSearch(bmExpr, FuncDefine, Type, Productions, StartSym)
    EndSearch = time.time()

    output_path = 'result.txt'
    with open(output_path, 'w') as f:
        f.write(Ans)
        # f.write("\nSynthesis time: %f\nSearch time: %f" %
        #        ((EndSearch-StartSynthesis), (EndSearch-StartSearch)))


if __name__ == '__main__':

    benchmarkFile = open(sys.argv[1])
    ProgramSynthesis(benchmarkFile)

    # Examples of counter-examples
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int 0)'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int x)'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int (+ x y))'))
