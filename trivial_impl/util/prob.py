import logging
from math import log

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


def get_transformed_context(statements, seq, params):
    return tuple(map(lambda x: feature_transform(x, params), get_context(statements, seq)))


COMPENSATION_RATE = 0.01


def get_production_prob(params, productions, statistics, start_symbol):
    non_terminals = productions.keys()
    derivation_symbols = {}
    possible_contexts = {}

    for non_terminal in non_terminals:
        derivation_symbols[non_terminal] = set(
            [feature_transform(production, params) for production in productions[non_terminal]])
        possible_contexts[non_terminal] = []

    possible_contexts[start_symbol].append(('{root}', '{empty}'))

    for non_terminal in non_terminals:
        for production in productions[non_terminal]:
            if type(production) is list:
                if production[1] in non_terminals:
                    possible_contexts[production[1]].append((production[0], '{empty}'))
                for i in range(2, len(production)):
                    if production[i] in non_terminals:
                        possible_contexts[production[i]].append(
                            (production[0], feature_transform(production[i - 1], params)))

    for non_terminal in non_terminals:
        for context in possible_contexts[non_terminal]:
            if context[1] in non_terminals:
                possible_contexts[non_terminal] += \
                    [(context[0], symbol) for symbol in derivation_symbols[context[1]]]
        possible_contexts[non_terminal] = set(possible_contexts[non_terminal])

    statistics_shared_count = {}
    for non_terminal in non_terminals:
        for context in possible_contexts[non_terminal]:
            for production in productions[non_terminal]:
                key = (feature_transform(production, params), context[0], context[1])
                if key not in statistics_shared_count:
                    statistics_shared_count[key] = 1
                else:
                    statistics_shared_count[key] += 1

    productions_with_prob = {}
    for non_terminal in non_terminals:

        productions_with_prob[non_terminal] = {}
        for context in possible_contexts[non_terminal]:

            total_appears = 0
            appears = []

            assert type(productions[non_terminal]) is list
            for production in productions[non_terminal]:

                if context[1] in non_terminals:
                    keys = set([
                        (feature_transform(production, params), context[0], feature_transform(symbol, params))
                        for symbol in derivation_symbols[context[1]]
                    ])
                else:
                    keys = {(feature_transform(production, params), context[0], context[1])}

                appears.append(0)

                for key in keys:
                    shared_count = statistics_shared_count[key]
                    if key not in statistics.keys():
                        appears[-1] += 0
                    else:
                        appears[-1] += (int(statistics[key] / shared_count))

                total_appears += appears[-1]

            compensation = int(total_appears * COMPENSATION_RATE)
            compensation = max(1, compensation)
            total_appears += compensation * len(productions[non_terminal])

            prob_in_context = []

            for i in range(len(productions[non_terminal])):
                production = productions[non_terminal][i]
                production_appears = appears[i]
                prob_in_context.append((production, (production_appears + compensation) / total_appears))

            productions_with_prob[non_terminal][context] = prob_in_context

    prob_upperbounds = {}
    for non_terminal in non_terminals:
        prob_upperbounds[non_terminal] = 0

    while True:
        updated = False

        for non_terminal in non_terminals:
            for context in possible_contexts[non_terminal]:
                for production, probability in productions_with_prob[non_terminal][context]:
                    next_upperbound = probability
                    if type(production) is list:
                        for symbol in production:
                            next_upperbound = next_upperbound * (
                                prob_upperbounds[symbol] if symbol in non_terminals else 1)
                    else:
                        next_upperbound = next_upperbound * (
                            prob_upperbounds[production] if production in non_terminals else 1)

                    if next_upperbound > prob_upperbounds[non_terminal]:
                        prob_upperbounds[non_terminal] = next_upperbound
                        updated = True
        if not updated:
            break

    return productions_with_prob, prob_upperbounds


def prob_to_dis(prob):
    return -log(prob, 2)


def get_statements_heuristics(statements, prob_upperbounds):
    log_prob_sum = 0

    for statement in statements:
        if type(statement) is list:
            log_prob_sum += get_statements_heuristics(statement, prob_upperbounds)
        elif statement in prob_upperbounds:
            log_prob_sum += prob_to_dis(prob_upperbounds[statement])

    return log_prob_sum
