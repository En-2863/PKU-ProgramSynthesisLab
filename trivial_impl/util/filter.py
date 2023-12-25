def commutative_and_ternary(statements) -> bool:
    """
    Given a statement check if it satisfies:
    1. If the operator is commutative, size of left operand <= right operand
    2. If the operator is ternary, expression in true condition doesn't equal to expression in false condition

    Args:
        statements (List(Symbol)):
            A list representing a statement, e.g. [[* Start Start]]

    Returns:
        True if the expression and its sub-expression satisfy all the rules above, else otherwise
    """

    def dfs(now_statement) -> (bool, int):
        results = []
        sizes = []
        for elem in now_statement:
            if type(elem) is list:
                (res, size) = dfs(elem)
            elif type(elem) is str:
                (res, size) = (True, 0)
            else:
                (res, size) = (True, 1)
            results.append(res)
            sizes.append(size)

        if now_statement[0] in ['+', '*', 'bvand', 'bvor', 'bvxor', 'bvadd', 'and', 'or']:
            assert len(now_statement) >= 3
            return all(results) and sizes[1] >= sizes[2], sum(sizes)

        if now_statement[0] in ['if0', 'ite']:
            if type(now_statement[2]) is tuple and type(now_statement[3]) is tuple:
                return all(results) and now_statement[2] != now_statement[3], sum(sizes)

        if now_statement[0] in ['<', '<=', '>', '>=', '=']:
            if type(now_statement[1]) is tuple and type(now_statement[2]) is tuple:
                return all(results) and now_statement[1] != now_statement[2], sum(sizes)

        return all(results), sum(sizes)

    return dfs(statements)[0]


class ExprFilter:
    """
        The ExprFilter class, a function class that can be called on an expression and return True if
        it satisfies all the rules added to it
    """
    def add_rule(self, rule):
        self.rules.append(rule)

    def __call__(self, expression) -> bool:
        # Return Ture if Expression satisfied all rules
        return all(map((lambda func: func(expression)), self.rules))

    def __init__(self):
        self.rules = []
        self.rules.append(commutative_and_ternary)
        pass


global_filter = ExprFilter()
