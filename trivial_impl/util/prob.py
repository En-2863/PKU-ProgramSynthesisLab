import logging

logging.basicConfig(filemode='w', filename='porb.log', level='INFO')


def get_seq(statements, seq):
    statement_now = statements
    for i in range(len(seq)):
        statement_now = statement_now[seq[i]]

    if type(statement_now) is list:
        return statement_now[0]

    return statement_now


def get_context(statements, seq):
    if len(seq) == 0:
        return '{root}', '{empty}'

    up = get_seq(statements, seq[:-1])
    if seq[-1] <= 1:
        left = '{empty}'
    else:
        left = get_seq(statements, seq[:-1] + [seq[-1] - 1])

    return up, left


def feature_transform(feature, params):
    if type(feature) is list:
        feature = feature[0]

    if type(feature) is tuple:
        feature = '{constant}'
    elif feature in params:
        feature = '{param}'

    assert type(feature) is str

    return feature


def context_transform(context, params):
    for i in range(len(context)):
        context[i] = feature_transform(context[i], params)

    return context


def get_production_prob(params, productions, statistics):
    logging.info(f'params: \n    {params}')
    logging.info(f'non-terminals: \n    {productions.keys()}')

    non_terminals = productions.keys()
    derivations = {}
    possible_contexts = {}

    for non_terminal in non_terminals:
        logging.info(f'non-terminal {non_terminal}:')
        derivations[non_terminal] = set(
            [feature_transform(symbol, params) for symbol in productions[non_terminal]])
        possible_contexts[non_terminal] = []
        logging.info(f'derivations: \n    {derivations[non_terminal]}')

    for non_terminal in non_terminals:
        for symbol in productions[non_terminal]:

            if type(symbol) is list:
                if symbol[1] in non_terminals:
                    possible_contexts[symbol[1]].append((symbol[0], '{empty}'))
                for i in range(2, len(symbol)):
                    if symbol[i] in non_terminals:
                        possible_contexts[symbol[i]].append((symbol[0], feature_transform(symbol[i - 1], params)))

    for non_terminal in non_terminals:
        for context in possible_contexts[non_terminal]:
            if context[1] in non_terminals:
                possible_contexts[non_terminal] += [(context[0], derivation) for derivation in derivations[context[1]]]

    logging.info(f'contexts: \n    {possible_contexts}')
