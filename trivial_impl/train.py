import sys
from functools import reduce

import src.sexp as sexp
from util.parsing import StripComments
from util.prob import *

import logging

logging.basicConfig(filename='train.log', filemode='w', level='INFO')

if __name__ == '__main__':
    # training
    inputFile = open(sys.argv[1])

    td = StripComments(inputFile)
    td_expr = sexp.sexp.parseString(td, parseAll=True).asList()[0]

    td_syntheses = [expr for expr in td_expr if expr[0] == 'synth-fun']
    td_defines = [expr for expr in td_expr if expr[0] == 'define-fun']
    td_params = reduce(lambda x, y: x + y, [synthesis[2] for synthesis in td_syntheses])
    td_grammar = td_syntheses[0][-1] # Only used for non-terminals, so just pick a random one
    func_bodies = [func[-1] for func in td_defines]

    params = set([param[0] for param in td_params])
    non_terminals = set([rule[0] for rule in td_grammar])

    logging.info(f'params: \n    {td_params}')
    logging.info(f'names: \n    {params}')
    logging.info(f'non-terminals: \n    {non_terminals}')

    logging.info(f'synth-fun: \n    {td_syntheses[0]}')

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
                    feature = feature_transform(symbol, params, non_terminals)
                    context = get_context(func_body, context_seq)
                    transformed_context = context_transform(context, params, non_terminals)
                    """
                    logging.info(f'dfs:    seq: {symbol_seq}')
                    logging.info(f'dfs:    symbol: {symbol}')
                    logging.info(f'dfs:    feature: {feature}')
                    logging.info(f'dfs:    context: {context}')
                    logging.info(f'dfs:    transformed: {transformed_context}')
                    """

                    if (feature, context[0], context[1]) in count:
                        count[(feature, context[0], context[1])] += 1
                    else:
                        count[(feature, context[0], context[1])] = 1


        # logging.info(f'func_body:{func_body}')
        dfs(func_body, [])

    logging.info('COUNT:')
    contexts = {}

    for elem in count:
        count_num = count[elem]
        logging.info(f'{elem}: {count_num}')
        if elem[1:] in contexts:
            contexts[elem[1:]] += count_num
        else:
            contexts[elem[1:]] = count_num

    logging.info('CONTEXTS:')

    for elem in contexts:
        logging.info(f'{elem}: {contexts[elem]}')

