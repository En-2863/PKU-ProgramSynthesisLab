bool_operand = ['=', '<=', '<', '>=', '>', 'and', 'or', 'not']
compare_operand = ['<=', '<', '>=', '>']
arith_operand = ['+', '-', '*', 'mod', 'bvor', 'bvand']
tenary_operand = ['ite']
NonTerminal = []


class Abstract():
    def __init__(self, Logic, FunCallList, SynFunc, Productions, Type):
        self.logic = Logic
        self.nonImplement = False
        self.func = FunCallList
        self.funcname = FunCallList[0]
        self.funcarg = FunCallList[1:]
        self.synfunc = SynFunc
        self.nonTerminal = Productions.keys()
        self.Productions = Productions  # with startsymbol
        self.Type = Type
        self.domain = None
        self.domain_max = None
        self.domain_min = None
        self.input_with_outut = []
        self.value = {}

        for signal in self.funcarg:
            self.value[signal] = []
        for signal in self.nonTerminal:
            self.value[signal] = []

        if self.logic == 'BV':
            self.nonImplement = True
            return
        else:
            if self.funcname == 'findIdx':
                array_num = len(self.funcarg) - 1
                # print(self.funcarg)
                # print(array_num)
                self.domain = [i-1 for i in range(array_num+3)]
                self.domain_min = -1
                self.domain_max = array_num + 1
                # construct input output pairs
                for i in range(array_num+1):
                    # print(i)
                    array = [j + 1 for j in range(array_num)]
                    # print(array)
                    input = array + [i]
                    # print(input)
                    ouput = [i]
                    self.input_with_outut.append([input, ouput])
                # print(self.input_with_outut)
                # compute value for nonterminal and variable
                for idx, pair in enumerate(self.input_with_outut):
                    input = pair[0]
                    for signal, val in zip(self.funcarg, input):
                        self.value[signal].append(val)
                    # compute nonterminals
                    for signal in self.nonTerminal:
                        if signal == 'My-Start-Symbol':
                            continue
                        elif Type[signal] == 'Int':
                            self.value[signal].append(self.domain)
                        elif Type[signal] == 'Bool':
                            self.value[signal].append([True, False])
            elif self.funcname.startswith('max'):
                arg_num = len(self.funcarg)
                self.domain = [i-1 for i in range(arg_num+2)]
                self.domain_min = -1
                self.domain_max = arg_num
                # construct input output pairs
                for idx, i in enumerate(self.domain[1:-1]):
                    input = [(j + idx) % arg_num for j in self.domain[1:-1]]
                    ouput = [arg_num - 1]
                    self.input_with_outut.append([input, ouput])
                # compute value for nonterminal and variable
                for idx, pair in enumerate(self.input_with_outut):
                    input = pair[0]
                    for signal, val in zip(self.funcarg, input):
                        self.value[signal].append(val)
                    # compute nonterminals
                    for signal in self.nonTerminal:
                        if signal == 'My-Start-Symbol':
                            continue
                        elif Type[signal] == 'Int':
                            self.value[signal].append(self.domain)
                        elif Type[signal] == 'Bool':
                            self.value[signal].append([True, False])
            else:
                self.nonImplement = True

    def clip_result(self, res):
        if res > self.domain_max:
            res = self.domain_max
        elif res < self.domain_min:
            res = self.domain_min
        return res

    def set_operand(self, s1, s2, operand):
        if not isinstance(s1, list):
            s1 = [s1]
        if not isinstance(s2, list):
            s2 = [s2]
        if operand == '^':
            return [i for i in s1 if i in s2]
        elif operand == 'v':
            s1_not_s2 = [i for i in s1 if i not in s2]
            return s1_not_s2 + s2
        elif operand == '+':
            return list(set([self.clip_result(i+j) for i in s1
                            for j in s2]))
        elif operand == '-':
            return list(set([self.clip_result(i-j) for i in s1
                            for j in s2]))
        elif operand == '*':
            return list(set([self.clip_result(i*j) for i in s1
                            for j in s2]))
        elif operand == 'mod':
            return list(set([self.clip_result(i % j) for i in s1
                            for j in s2 if j != 0]))
        elif operand == '<':
            s1_max = max(s1)
            s1_min = min(s1)
            s2_max = max(s2)
            s2_min = min(s2)
            if s1_max < s2_min:
                return True
            elif s1_min >= s2_max:
                return False
            else:
                return [True, False]
        elif operand == '<=':
            s1_max = max(s1)
            s1_min = min(s1)
            s2_max = max(s2)
            s2_min = min(s2)
            if s1_max <= s2_min:
                return True
            elif s1_min > s2_max:
                return False
            else:
                return [True, False]

    def evaluate(self, Stmt, input_idx):
        if isinstance(Stmt, str):
            return self.value[Stmt][input_idx]
        elif isinstance(Stmt, tuple):
            # print(Stmt)
            return Stmt[1]
        elif isinstance(Stmt, list):
            if Stmt[0] in bool_operand:
                S1 = self.evaluate(Stmt[1], input_idx)
                # print(f"S1: {S1}")
                if len(Stmt) == 3:
                    S2 = self.evaluate(Stmt[2], input_idx)
                    # print(f"S2: {S2}")
                if Stmt[0] == '=':
                    ret = self.set_operand(S1, S2, '^')
                    if len(ret) == 0:
                        return False
                    else:
                        return True
                elif Stmt[0] == '<':
                    ret = self.set_operand(S1, S2, '<')
                    return ret
                elif Stmt[0] == '>=':
                    ret = self.set_operand(S2, S1, '<=')
                    return ret
                elif Stmt[0] == '>':
                    ret = self.set_operand(S2, S1, '<')
                    return ret
                elif Stmt[0] == '<=':
                    ret = self.set_operand(S1, S2, '<=')
                    return ret
                elif Stmt[0] == 'and':
                    if S1 is True and S2 is True:
                        return True
                    elif S1 is False or S2 is False:
                        return False
                    else:
                        return [True, False]
                elif Stmt[0] == 'or':
                    if S1 is False and S2 is False:
                        return False
                    elif S1 is True or S2 is True:
                        return True
                    else:
                        return [True, False]
                elif Stmt[0] == 'not':
                    if S1 is True:
                        return False
                    elif S1 is False:
                        return True
                    else:
                        return [True, False]
            elif Stmt[0] in arith_operand:
                S1 = self.evaluate(Stmt[1], input_idx)
                # print(f"S1: {S1}")
                if len(Stmt) == 3:
                    S2 = self.evaluate(Stmt[2], input_idx)
                    # print(f"S2: {S2}")
                if Stmt[0] == '+':
                    return self.set_operand(S1, S2, '+')
                elif Stmt[0] == '-':
                    return self.set_operand(S1, S2, '-')
                elif Stmt[0] == '*':
                    return self.set_operand(S1, S2, '*')
                elif Stmt[0] == 'mod':
                    return self.set_operand(S1, S2, 'mod')
            elif Stmt[0] in tenary_operand:
                if Stmt[0] == 'ite':
                    BoolExp = self.evaluate(Stmt[1], input_idx)
                    S1 = self.evaluate(Stmt[2], input_idx)
                    S2 = self.evaluate(Stmt[3], input_idx)
                    if self.funcname == 'findIdx':
                        # print(Stmt[2])
                        #if (not isinstance(BoolExp, str)) \
                        #        and BoolExp[0] not in compare_operand \
                        #        and not isinstance(BoolExp[1], str):
                        #    return []
                        if not isinstance(Stmt[2], tuple) and \
                            (isinstance(Stmt[2], str) and
                             Stmt[2] not in self.nonTerminal):
                            return []
                    elif self.funcname.startswith('max'):
                        if not isinstance(Stmt[2], str):
                            return []
                    if BoolExp is True:
                        return S1
                    elif BoolExp is False:
                        return S2
                    else:
                        return self.set_operand(S1, S2, 'v')
        else:
            # print(Stmt)
            raise NotImplementedError

    def __call__(self, Stmt):
        if self.nonImplement is True:
            return True
        if isinstance(Stmt, list) and len(Stmt) == 1:
            Stmt = Stmt[0]
        for idx, pair in enumerate(self.input_with_outut):
            output = pair[1][0]
            #print(f"stmt: {Stmt}")
            out = self.evaluate(Stmt, idx)
            #print(f"input: {pair[0]}")
            #print(f"out: {out}")
            #print(f"output: {output}")
            if isinstance(out, list):
                if output not in out:
                    return False
            else:
                if output != out:
                    return False

        return True
