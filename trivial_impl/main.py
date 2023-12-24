import sys,os, time
import src.sexp as sexp
import util.translator as translator
from util.parsing import ParseSynFunc, StripComments
from util.priority_queue import Priority_Queue, Select
from util.counterexample import UpdateSearchSpace
from util.filter import Filter
from util.prob import *

from train import train

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
        # Recursivly search the non-terminals, e.g. [* Start Start]
        if type(Stmts[i]) is list:
            TryExtend = Extend(Stmts[i], Productions)
            if len(TryExtend) > 0:
                ret.extend(Stmts[0:i] + [extended] + Stmts[i+1:]
                           for extended in TryExtend
                           if Filter(Stmts[0:i] + [extended] + Stmts[i+1:]))
        # Terminals
        elif type(Stmts[i]) is tuple:
            continue
        # Unfold the non-terminals
        elif Stmts[i] in Productions:
            ret.extend(Stmts[0:i] + [extended] + Stmts[i+1:]
                       for extended in Productions[Stmts[i]]
                       if Filter(Stmts[0:i] + [extended] + Stmts[i+1:]))
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

    # Top-down search
    while len(BfsQueue) != 0:
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


def ProgramSynthesis(benchmarkFile):
    StartSynthesis=time.time()
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


    if len(sys.argv) > 2:
        trainData = open(sys.argv[2])
        statistics = train(trainData)
        get_production_prob(set([param[0] for param in SynFunExpr[2]]), Productions, statistics)

    StartSearch=time.time()
    Ans = Search(checker, FuncDefine, Type, Productions, StartSym)
    EndSearch=time.time()
    print(Ans)


    with open('./outputs/'+'CEGIS_result_'+os.path.split(str(benchmarkFile))[-1]+'.txt', 'w') as f:
        f.write(Ans)
        f.write("\nSynthesis time: %f\nSearch time: %f"%((EndSearch-StartSynthesis),(EndSearch-StartSearch)))


if __name__ == '__main__':

    benchmarkFile = open(sys.argv[1])
    ProgramSynthesis(benchmarkFile)

    # Examples of counter-examples
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int 0)'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int x)'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int (+ x y))'))
