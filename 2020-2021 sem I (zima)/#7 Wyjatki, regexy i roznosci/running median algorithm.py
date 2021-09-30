# Created by Marcin "Cozoob" Kozub 30.09.2021
# Doesn't work
from queue import PriorityQueue
import heapq as hq

def running_median(array):
    min_heap = []
    hq.heapify(min_heap)
    max_heap = PriorityQueue()
    medians = []

    for number in array:
        add_number(number, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        medians.append(get_median(min_heap, max_heap))

    return medians


def add_number(number, min_heap, max_heap):
    if len(min_heap) == 0:
        min_heap.append(number)
    else:
        lower = hq.heappop(min_heap)
        if lower < number:
            max_heap.put(number)
        else:
            hq.heappush(min_heap, number)

        hq.heappush(min_heap, lower)

def rebalance(min_heap, max_heap):

    if len(min_heap) - max_heap.qsize() > 2:
        lower = hq.heappop(min_heap)
        max_heap.put(lower)


def get_median(min_heap, max_heap):
    lower = hq.heappop(min_heap)
    if not max_heap.empty():
        bigger = max_heap.get()
    else:
        bigger = 0
    hq.heappush(min_heap, lower)
    max_heap.put(bigger)

    if not max_heap.empty() and len(min_heap) == max_heap.qsize():
        return (lower + bigger) / 2
    elif len(min_heap) > max_heap.qsize():
        return lower
    else:
        return bigger

if __name__ == '__main__':
    arr = [3,2,6,72,45,8,4]
    print(running_median(arr))