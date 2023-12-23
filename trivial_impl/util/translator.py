from z3 import *
import random

# set it nonzero to debug
verbose = 0


def DeclareVar(sort, name):
    if sort == "Int":
        return Int(name)
    if sort == 'Bool':
        return Bool(name)


def getSort(sort):
    if sort == "Int":
        return IntSort()
    if sort == "Bool":
        return BoolSort()
    if type(sort) is list and sort[0] == "BitVec":  # sygus 1.0 format: (BitVec 64)
        return BitVecSort(sort[1][1])
    if type(sort) is list and sort[0] == "_" and sort[1] == "BitVec":  # sygus 2.0 format: (_ BitVec 64)
        return BitVecSort(sort[2][1])
    print("Error: unknown sort", sort)
    assert False


def constToString(sort, value):
    # print(sort, value)
    if sort == "Int" or sort == "Bool":
        return str(value)
    if type(sort) is list and sort[0] == "_":
        sort = sort[1:]
    if type(sort) is list and sort[0] == "BitVec":
        l = sort[1][1]
        assert l % 4 == 0
        v = hex(value)[2:]
        v = "#x" + "0" * (l // 4 - len(v)) + v
        return v
    print("Error: unknown sort", sort)
    assert False


def toString(Expr, Bracket=True, ForceBracket=False):
    if type(Expr) is str:
        return Expr
    if type(Expr) is tuple:
        return constToString(Expr[0], Expr[1])
    if Expr[0] == "BitVec":
        return "(_ BitVec " + str(Expr[1][1]) + ")"
    subexpr = []
    for expr in Expr:
        if type(expr) is list:
            subexpr.append(toString(expr, ForceBracket=ForceBracket))
        elif type(expr) is tuple:
            subexpr.append(constToString(expr[0], expr[1]))
        else:
            subexpr.append(expr)

    if not Bracket:
        return "%s" % (' '.join(subexpr))
    # Avoid Redundant Brackets
    if ForceBracket:
        return "(%s)" % (' '.join(subexpr))
    if len(subexpr) == 1:
        return "%s" % (' '.join(subexpr))
    else:
        return "(%s)" % (' '.join(subexpr))


def ReadQuery(bmExpr):
    SynFunExpr = []
    VarDecMap = {}
    Constraints = []
    FunDefMap = {}
    AuxFuns = []
    for expr in bmExpr:
        if len(expr) == 0:
            continue
        elif expr[0] == 'synth-fun':
            SynFunExpr = expr
        elif expr[0] == 'declare-var':
            VarDecMap[expr[1]] = expr
        elif expr[0] == 'constraint':
            Constraints.append(expr)
        elif expr[0] == 'define-fun':
            FunDefMap[expr[1]] = expr
            AuxFuns.append(toString(expr, ForceBracket=True))

    
  

    VarTable = {}
    # Declare Var
    for var in VarDecMap:
        VarTable[var] = DeclareVar(VarDecMap[var][2], var)

    if verbose == 1:
        print(SynFunExpr)
        print(VarDecMap)
        print(FunDefMap)
        print(Constraints)
        print(AuxFuns)
        print(VarTable)

    # Declare Target Function
    class SynFunction:
        def __init__(self, SynFunExpr):
            self.name = SynFunExpr[1]
            self.argList = SynFunExpr[2]
            self.retSort = SynFunExpr[3]
            self.Sorts = []
            for expr in self.argList:
                self.Sorts.append(getSort(expr[1]))
            self.Sorts.append(getSort(self.retSort))
            self.targetFunction = Function('__TARGET_FUNCTION__', *(self.Sorts))

    synFunction = SynFunction(SynFunExpr)

    class Checker:
        def __init__(self, VarTable, synFunction, Constraints, AuxFuns):

            self.VarTable = VarTable

            self.synFunction = synFunction

            self.Constraints = Constraints

            self.AuxFuns = AuxFuns

            self.solver = Solver()

            self.counterexample=[]

        def addConstraint(self, model):
            values=[]
            numofargv=len(self.VarTable)
            for key in self.VarTable:
                value=model.evaluate(self.VarTable[key])
                if not self.VarTable[key]==value:
                    values.append(value)
                else:
                    values.append(random.randint(-50, 50))# use random Int to replace the unknow argument
            funcname=model[len(model)-1]
            func=model[funcname]

            # ugly implementation...
            if(numofargv==1):
                values.append(model.eval(funcname(values[0])))
            elif(numofargv==2):
                values.append(model.eval(funcname(values[0], values[1])))
            elif(numofargv==3):
                values.append(model.eval(funcname(values[0], values[1], values[2])))
            elif(numofargv==4):
                values.append(model.eval(funcname(values[0], values[1], values[2], values[3])))
            elif(numofargv==5):
                values.append(model.eval(funcname(values[0], values[1], values[2], values[3], values[4])))

            self.counterexample.append(values)

            if verbose == 3:
                    print("check input_output pair")
                    print(func.else_value())
                    print(values)

            
        def check(self, funcDefStr):
            spec_smt2_head = self.AuxFuns + [funcDefStr]
            spec_smt2_originConstrains=[]

            for constraint in Constraints:
                spec_smt2_originConstrains.append('(assert %s)' % (toString(constraint[1:])))

            for ce in self.counterexample:
                counterexampleConstrains=[]
                index=0
                for var in VarTable:
                    counterexampleConstrains.append('(assert (= %s %s))'%(var, str(ce[index])))
                    index+=1

                self.solver.push()
                spec_smt2 = spec_smt2_head+counterexampleConstrains+spec_smt2_originConstrains
                spec_smt2 = '\n'.join(spec_smt2)
                spec = parse_smt2_string(spec_smt2, decls=dict(self.VarTable))
                spec = And(spec)
                self.solver.add(spec)
                res=self.solver.check()
                self.solver.pop()

                if res == unsat:
                    return []
                    


            self.solver.push()
            spec_smt2 = spec_smt2_head+spec_smt2_originConstrains
            spec_smt2 = '\n'.join(spec_smt2)   
            spec = parse_smt2_string(spec_smt2, decls=dict(self.VarTable))
            if verbose == 2:
                print("spec:", spec_smt2)
            if verbose == 3:
                print("funcDefStr:", funcDefStr)
            spec = And(spec)
            self.solver.add(Not(spec))
            

            res = self.solver.check()
            if res == unsat:
                self.solver.pop()
                return None
            else:
                model = self.solver.model()
                self.addConstraint(model)
                self.solver.pop()
                return model

    checker = Checker(VarTable, synFunction, Constraints, AuxFuns)
    return checker
