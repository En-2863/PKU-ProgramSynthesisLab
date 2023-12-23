import heapq


def list_count(x, layer, nonterminal):
    assert type(x) is list
    ret = 0
    for item in x:
        if type(item) is list:
            ret += list_count(item, layer+1, nonterminal)
            ret += (layer**2)
        else:
            ret += 1 if item not in nonterminal else 100*layer
    return ret


class Priority_Queue():
    def __init__(self, nonterminal):
        self.queue = []
        self.index = 0
        self.nonterminal = list(nonterminal)

    def __len__(self):
        return len(self.queue)

    def add_item(self, x):
        priority = 0
        if type(x) is list:
            priority = list_count(x, 0, self.nonterminal)  # choose list length as priority
            # print(priority, x)
        else:
            priority = 1 if x not in self.nonterminal else 100
        heapq.heappush(self.queue, [priority, self.index, x])
        self.index += 1

    def pop_item(self):
        if len(self.queue) == 0:
            return None
        output = heapq.heappop(self.queue)
        # print(output)
        return output[2]


def Select(BfsQueue: Priority_Queue):
    # TODO select the most promising answer from the queue
    return BfsQueue.pop_item()
