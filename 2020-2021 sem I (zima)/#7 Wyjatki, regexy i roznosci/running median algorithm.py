# Created by Marcin "Cozoob" Kozub 30.09.2021
# Doesn't work
from heapq import heappop, heappush

def running_median(array):
    min_heap = []
    max_heap = []
    medians = []

    for number in array:
        add_number(number, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        medians.append(get_median(min_heap, max_heap))

    return medians

def add_number(number, min_heap, max_heap):
    if not max_heap or number > max_heap[0]:
        heappush(max_heap, number)
    else:
        heappush(min_heap, -number) # we add a negative number to "create" a min_heap

def rebalance(min_heap, max_heap):
    if len(min_heap) - len(max_heap) > 1:
        heappush(max_heap, -heappop(min_heap))  # the min_heap has too many elements
    elif len(max_heap) - len(min_heap) > 1:
        heappush(min_heap, -heappop(max_heap))  # the max_heap has too many elements


def get_median(min_heap, max_heap):
    if len(max_heap) == len(min_heap):
        return (max_heap[0] - min_heap[0]) / 2
    elif len(max_heap) > len(min_heap):
        return max_heap[0]
    else:
        return -min_heap[0]

if __name__ == '__main__':
    arr = [3,2,6,72,45,8,4]
    print(running_median(arr))