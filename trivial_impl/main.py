import sys
import sexp
import pprint
import translator
from priority_queue import Priority_Queue


def Extend(Stmts, Productions):
    ret = []
    for i in range(len(Stmts)):
        if type(Stmts[i]) is list:
            TryExtend = Extend(Stmts[i], Productions)
            if len(TryExtend) > 0:
                for extended in TryExtend:
                    ret.append(Stmts[0:i]+[extended]+Stmts[i+1:])
        elif type(Stmts[i]) is tuple:
            continue
        elif Stmts[i] in Productions:
            for extended in Productions[Stmts[i]]:
                ret.append(Stmts[0:i]+[extended]+Stmts[i+1:])
    return ret


def stripComments(bmFile):
    noComments = '(\n'
    for line in bmFile:
        line = line.split(';', 1)[0]
        noComments += line
    return noComments + '\n)'


if __name__ == '__main__':
    benchmarkFile = open(sys.argv[1])
    bm = stripComments(benchmarkFile)
    # print(bm)
    # Parse string to python list
    bmExpr = sexp.sexp.parseString(bm, parseAll=True).asList()[0]
    # pprint.pprint(bmExpr)
    checker = translator.ReadQuery(bmExpr)
    # print (checker.check('(define-fun f ((x Int)) Int (mod (* x 3) 10)  )'))
    # raw_input()
    SynFunExpr = []
    StartSym = 'My-Start-Symbol'  # virtual starting symbol
    for expr in bmExpr:
        if len(expr) == 0:
            continue
        elif expr[0] == 'synth-fun':
            SynFunExpr = expr
    FuncDefine = ['define-fun']+SynFunExpr[1:4]  # copy function signature
    # print(FuncDefine)
    # BfsQueue = [[StartSym]] #Top-down
    BfsQueue = Priority_Queue()
    BfsQueue.add_item([StartSym])
    Productions = {StartSym: []}
    Type = {StartSym: SynFunExpr[3]}  # set starting symbol's return type
    for NonTerm in SynFunExpr[4]:  # SynFunExpr[4] is the production rules
        NTName = NonTerm[0]
        NTType = NonTerm[1]
        if NTType == Type[StartSym]:
            Productions[StartSym].append(NTName)
        Type[NTName] = NTType
        Productions[NTName] = NonTerm[2]
    Count = 0
    TE_memory = set()
    while len(BfsQueue) != 0:
        Curr = BfsQueue.pop_item()
        # print("extend:", Curr)
        TryExtend = Extend(Curr, Productions)
        if len(TryExtend) == 0:  # Nothing to
            # print(FuncDefine)
            # print("find", Curr)

            # use Force Bracket = True on function definition. MAGIC CODE.
            # DO NOT MODIFY THE ARGUMENT ForceBracket = True.
            FuncDefineStr = translator.toString(FuncDefine, ForceBracket=True)
            CurrStr = translator.toString(Curr)
            # SynFunResult = FuncDefine+Curr
            # Str = translator.toString(SynFunResult)

            # insert Program just before the last bracket ')'
            Str = FuncDefineStr[:-1] + ' ' + CurrStr+FuncDefineStr[-1]
            Count += 1
            # print (Count)
            # print (Str)
            # if Count % 100 == 1:
            #     print (Count)
            #     print (Str)
            #     raw_input()
            # print '1'
            counterexample = checker.check(Str)
            # print counterexample
            if counterexample is None:  # No counter-example
                Ans = Str
                break
            # print '2'
        # print(TryExtend)
        # raw_input()
        # BfsQueue+=TryExtend
        TE_set = set()
        for TE in TryExtend:
            TE_str = str(TE)
            if TE_str not in TE_set and TE_str not in TE_memory:
                BfsQueue.add_item(TE)
                TE_memory.add(TE_str)
                TE_set.add(TE_str)

    print(Ans)
    with open('result.txt', 'w') as f:
        f.write(Ans)

    # Examples of counter-examples
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int 0)'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int x)'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int (+ x y))'))
    # print (checker.check('(define-fun max2 ((x Int) (y Int)) Int (ite (<= x y) y x))'))
