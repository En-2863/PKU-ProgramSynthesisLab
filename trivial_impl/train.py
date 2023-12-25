from functools import reduce

import src.sexp as sexp
from util.parsing import StripComments
from util.prob import *


def train(training_data):
    # training
    td_expr = sexp.sexp.parseString(StripComments(training_data), parseAll=True).asList()[0]

    td_syntheses = [expr for expr in td_expr if expr[0] == 'synth-fun']
    td_defines = [expr for expr in td_expr if expr[0] == 'define-fun']
    td_params = reduce(lambda x, y: x + y, [synthesis[2] for synthesis in td_syntheses])

    func_bodies = [func[-1] for func in td_defines]
    params = set([param[0] for param in td_params])

    count = {}
    for func_body in func_bodies:

        def dfs(statements_now, seq):
            for i in range(len(statements_now)):
                if type(statements_now[i]) is list:
                    dfs(statements_now[i], seq + [i])
                else:
                    if i == 0:
                        symbol_seq = seq + [i]
                        context_seq = seq
                    else:
                        symbol_seq = seq + [i]
                        context_seq = seq + [i]

                    symbol = get_seq(func_body, symbol_seq)
                    feature = feature_transform(symbol, params)
                    context = tuple(map(lambda x: feature_transform(x, params), get_context(func_body, context_seq)))

                    if (feature, context[0], context[1]) in count:
                        count[(feature, context[0], context[1])] += 1
                    else:
                        count[(feature, context[0], context[1])] = 1

        dfs(func_body, [])

    return count
