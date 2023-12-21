def commutative_and_ternary(expression) -> bool:
    """
    Given a statement check if it satisfies:
    1. If the operator is commutative, size of left operand <= right operand
    2. If the operator is ternary, expression in true condition doesn't equal to expression in false condition

    Args:
        Stmts (List(Symbol)):
            A list representing a statement, e.g. [[* Start Start]]

    Returns:
        True if the expression and its sub-expression satisfie all the rules above, else otherwise
    """

    def commutative_dfs(now_expr) -> (bool, int):
        results = []
        sizes = []
        for elem in now_expr:
            if type(elem) is list:
                (res, size) = commutative_dfs(elem)
            elif type(elem) is str:
                (res, size) = (True, 0)
            else:
                (res, size) = (True, 1)
            results.append(res)
            sizes.append(size)

        if now_expr[0] in ['+', '*', 'bvand', 'bvor', 'bvxor', 'bvadd', 'and', 'or']:
            assert len(now_expr) >= 3
            return all(results) and sizes[1] <= sizes[2], sum(sizes)

        if expression[0] in ['if0', 'ite']:
            if type(expression[2]) is tuple and type(expression[3]) is tuple:
                return all(results) and expression[2] != expression[3], sum(sizes)

        return all(results), sum(sizes)

    return commutative_dfs(expression)[0]


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
