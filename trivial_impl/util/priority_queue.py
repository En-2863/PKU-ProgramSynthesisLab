import heapq


def list_count(x, layer):
    assert type(x) is list
    ret = 0
    for item in x:
        if type(item) is list:
            ret += list_count(item, layer+1)
            ret += layer**2
        else:
            ret += 1
    return ret


class Priority_Queue():
    def __init__(self):
        self.queue = []
        self.index = 0

    def __len__(self):
        return len(self.queue)

    def add_item(self, x):
        priority = 0
        if type(x) is list:
            priority = list_count(x, 0)  # choose list length as priority
        else:
            priority = 1
        heapq.heappush(self.queue, [priority, self.index, x])
        self.index += 1

    def pop_item(self):
        output = heapq.heappop(self.queue)
        return output[2]


def Select(BfsQueue: Priority_Queue):
    # TODO select the most promising answer from the queue
    return BfsQueue.pop_item()
