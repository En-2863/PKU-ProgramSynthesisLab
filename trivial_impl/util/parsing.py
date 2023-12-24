def StripComments(bmFile):
    """Strip comments from file

    Args:
        bmFile: Target file descriptor

    Returns:
        str: File content without comments
    """
    noComments = '(\n'
    for line in bmFile:
        line = line.split(';', 1)[0]
        noComments += line
    return noComments + '\n)'


def SortProuctions(Nonterm):
    NewNonTerm = []
    iteTerm = []
    operTerm = []
    hasIte = False
    for term in Nonterm:
        if type(term) is list:
            if term[0] == 'ite' or term[0] == 'if0':
                if term[0] == 'ite':
                    hasIte = True
                iteTerm.append(term)
            # elif term[0] == '>=' and '<' not in operTerm:
            #     operTerm.append(term)
            # elif term[0] == '<=' and '>' not in operTerm:
            #     operTerm.append(term)
            # elif term[0] == '<' and '>=' not in operTerm:
            #     operTerm.append(term)
            # elif term[0] == '>' and '<=' not in operTerm:
            #     operTerm.append(term)
            else:
                operTerm.append(term)
        else:
            NewNonTerm.append(term)
    NewNonTerm.extend(iteTerm)
    NewNonTerm.extend(operTerm)
    return Nonterm, hasIte

def ParseSynFunc(SynFunExpr, StartSym='My-Start-Symbol'):
    """Parse synfunc and get the return type of symbols and production rules.

    Args:
        SynFunExpr (List(Syn-func Expressions)):
            Target synthesized function and its production rules
        StartSym (str, optional):
            A symbol to start with. Defaults to 'My-Start-Symbol'.

    Returns:
        Type (Dict(Symbol: Type)): Return type of symbols
        Productions (Dict(Symbol: List(Expressions))):
            Production rules for given symbols
    """
    Productions = {StartSym: []}                    # rules for extending
    Type = {StartSym: SynFunExpr[3]}                # symbol's return type
    Ite = False

    # SynFunExpr[4] is the production rules
    # NonTerm: (Start, Int, (x, y, 0...)) / (StartBool, Bool, (and, or...))
    for NonTerm in SynFunExpr[4]:
        NTName, NTType = NonTerm[0], NonTerm[1]

        # Make sure start with the right return value
        if NTType == Type[StartSym]:
            Productions[StartSym].append(NTName)

        Type[NTName] = NTType
        Productions[NTName], hasIte = SortProuctions(NonTerm[2])

        if hasIte is True:
            Ite = True

    return Type, Productions, Ite
