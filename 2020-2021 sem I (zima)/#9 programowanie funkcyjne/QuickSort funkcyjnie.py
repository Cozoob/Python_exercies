# Created by Marcin "Cozoob" Kozub 22.11.2021
import random
from random import randint, seed

def QuickSort(left, right, arr):
    if len(arr) <= 1:
        return arr

    if left < right:
        middle = partition(left, right, arr)
        QuickSort(left, middle - 1, arr)
        QuickSort(middle + 1, right, arr)


def partition(left, right, arr):
    if left >= right:
        return left

    pivot = arr[right]
    j = left

    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    arr[j], arr[right] = arr[right], arr[j]
    return j



if __name__ == '__main__':
    seed(42)
    arr = [randint(-3,10) for _ in range(12)]
    print(arr)
    QuickSort(0, len(arr)-1,arr)
    print(arr)