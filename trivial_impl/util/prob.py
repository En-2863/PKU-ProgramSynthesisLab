import copy


def get_seq(statements, seq):
    statement_now = statements
    for i in range(len(seq)):
        statement_now = statement_now[seq[i]]

    if type(statement_now) is list:
        return statement_now[0]

    return statement_now


def get_context(statements, seq):
    if len(seq) == 0:
        return ['{root}', '{empty}']

    up = get_seq(statements, seq[:-1])
    if seq[-1] <= 1:
        left = '{empty}'
    else:
        left = get_seq(statements, seq[:-1] + [seq[-1] - 1])

    return [up, left]


def feature_transform(feature, params, non_terminals):
    if type(feature) is list:
        feature = feature[0]

    if type(feature) is tuple:
        feature = '{constant}'
    elif feature in params:
        feature = '{param}'
    elif feature in non_terminals:
        feature = '{non_terminal}'

    assert type(feature) is str

    return feature


def context_transform(context, params, non_terminals):
    for i in range(len(context)):
        context[i] = feature_transform(context[i], params, non_terminals)

    return context
