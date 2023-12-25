from z3 import *

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


def is_const(signal):
    if type(signal) is not tuple or len(signal) != 2:
        return False
    if type(signal[0]) is list and (signal[0][0] == 'BitVec'):
        if type(signal[1]) is int:
            return True
    elif signal[0] == 'Int' and type(signal[1]) is int:
        return True
    return False


def check_operand(constraint, funcname, argnum):
    if len(constraint) != 3:
        return False
    operator = constraint[0]
    operand_l = constraint[1]
    operand_r = constraint[2]
    if operator != '=':
        return False
    if len(operand_l) != argnum + 1 or operand_l[0] != funcname:
        return False
    for i in range(argnum):
        if is_const(operand_l[i + 1]) is False:
            return False
    if type(operand_r) is not tuple or is_const(operand_r) is False:
        return False

    return True


def ReadQuery(bmExpr):
    SynFunExpr = []
    VarDecMap = {}
    Constraints = []
    FunDefMap = {}
    AuxFuns = []
    FuncCallList = []
    Logic = None
    CEGIS_count = {}
    for expr in bmExpr:
        if len(expr) == 0:
            continue
        elif expr[0] == 'set-logic':
            Logic = expr[1]
        elif expr[0] == 'synth-fun':
            SynFunExpr = expr
            FuncCallList.append(SynFunExpr[1])
            for s in SynFunExpr[2]:
                FuncCallList.append(s[0])
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
            self.Constraints = []
            self.AuxFuns = AuxFuns
            self.SmtConstraints = []
            self.CounterExample = []
            self.solver = Solver()
            self.funcname = synFunction.name
            self.argnum = len(synFunction.argList)

            for constraints in Constraints:
                self.Constraints.append('(assert %s)'
                                        % (toString(constraints[1:])))
                if len(constraints) < 2:
                    continue
                if len(constraints[1]) == 3 and \
                        check_operand(constraints[1], self.funcname, self.argnum):
                    self.SmtConstraints.append('(assert %s)'
                                               % (toString(constraints[1:])))

        def addConstraint(self, model):
            values = []
            if len(self.VarTable.keys()) == 0:
                return
            for key in self.VarTable:
                value = model.eval(self.VarTable[key])
                if isinstance(value, IntNumRef):
                    sexpr = value.sexpr()
                    if sexpr.startswith('('):
                        sexpr = sexpr[1:-1]
                    val_str = sexpr.replace(' ', '')
                    values.append(int(val_str))
                else:
                    return

            funcname = model[len(model)-1]
            func = model[funcname]

            values.append(model.eval(funcname(values)))
            # MAGIC CODE
            if len(values) == 2 and values[0] == 0 and values[1] == 0:
                return

            Args = [str(var) for var in values]
            Constraint = f"(assert (= {Args[-1]} ({self.synFunction.name} {' '.join(Args[:-1])})))"
            #print(Constraint)
            CEGIS_count[len(self.CounterExample)] = 0
            self.CounterExample.append(Constraint)
            # print(len(self.counterexample))
            # print(f"counter: {len(self.counterexample)}")

            if verbose == 3:
                print("check input_output pair")
                print(func.else_value())
                print(values)

        def check(self, funcDefStr):
            spec_smt2_head = self.AuxFuns + [funcDefStr]
            spec_smt2_originConstrains = self.Constraints

            # Check satisfy original constraints with specific format:
            # funcname (const...) = const
            for constraint in self.SmtConstraints:
                # print(constraint)
                self.solver.push()
                spec_smt2 = spec_smt2_head + [constraint]
                spec_smt2 = '\n'.join(spec_smt2)
                spec = parse_smt2_string(spec_smt2, decls=dict(self.VarTable))
                spec = And(spec)
                self.solver.add(spec)
                res = self.solver.check()
                self.solver.pop()

                if res == unsat:
                    return []

            # Check satisfy CEGIS constraints
            for idx, ce in enumerate(self.CounterExample):
                self.solver.push()
                spec_smt2 = spec_smt2_head + [ce]
                spec_smt2 = '\n'.join(spec_smt2)
                spec = parse_smt2_string(spec_smt2)
                spec = And(spec)
                self.solver.add(spec)
                res = self.solver.check()
                self.solver.pop()

                if res == sat:
                    CEGIS_count[idx] += 1
                    if CEGIS_count[idx] % 5000 == 0:
                        print(f"{ce}: {CEGIS_count[idx]}")
                    return []

            self.solver.push()
            spec_smt2 = spec_smt2_head + spec_smt2_originConstrains
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
                # print(model)
                self.addConstraint(model)
                self.solver.pop()
                return model

    checker = Checker(VarTable, synFunction, Constraints, AuxFuns)
    return checker, Logic, FuncCallList, SynFunExpr
