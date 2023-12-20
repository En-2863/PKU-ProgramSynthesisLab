import logging


# logging.basicConfig(filename="filter.log", level='INFO')

def commutative(expression) -> bool:
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

        if now_expr[0] in ['+', '*']:
            assert len(now_expr) >= 3
            return results[1] and results[2] and sizes[1] <= sizes[2], sum(sizes)

        return all(results), sum(sizes)

    return commutative_dfs(expression)[0]


class ExprFilter:

    def add_rule(self, rule):
        self.rules.append(rule)

    def __call__(self, expression) -> bool:
        # Return Ture if Expression satisfied all rules
        return all(map((lambda func: func(expression)), self.rules))

    def __init__(self):
        self.rules = []
        self.rules.append(commutative)
        pass


global_filter = ExprFilter()
