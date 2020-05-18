'''
Project 1
CS 2420
Ryan Balog
'''
from random import seed, sample
from time import perf_counter
from math import sqrt
from recursioncounter import RecursionCounter


def create_lyst():
    '''returns a large list to main()'''
    print("Generating list...")
    seed(0)
    lyst = sample(range(10000000), k=1000000)
    lyst.sort()

    print("Generated list of size ", len(lyst))
    return lyst


def linear_search(lyst, target):
    '''searches for a target value in lyst and returns if found'''
    if isinstance(target, int) == False:
        raise ValueError("Target must be an integer")
    for index in lyst:
        if isinstance(index, int) == False:
            raise ValueError("List values must be integer")
        if index == target:
            return True
    return False


def recursive_binary_search(lyst, target):
    '''calls binary_helper() with initial low/high indexes from lyst'''
    if isinstance(target, int) == False:
        raise ValueError("Target must be integer")
    return recursive_binary_search_helper(lyst, target, 0, len(lyst)-1)


def recursive_binary_search_helper(lyst, target, low, high):
    '''performs binary search, recursively, to find if target exists in lyst'''
    RecursionCounter()
    mid = int((low + high) / 2)

    if low > high or high < low:
        return False
    if isinstance(lyst[mid], int) == False:
        raise ValueError("List values must be an integer")
    if lyst[mid] == target:
        return True
    if target < lyst[mid]:
        return recursive_binary_search_helper(lyst, target, low, mid-1)
    else:
        return recursive_binary_search_helper(lyst, target, mid+1, high)


def jump_search(lyst, target):
    '''performs jump search to find if target exists in lyst'''
    if isinstance(target, int) == False:
        raise ValueError("Target must be an integer")

    step = int(sqrt(len(lyst)))
    first = 0
    last = first + step

    while True:
        if isinstance(lyst[0] or lyst[-1], int) == False:
            raise ValueError("List values must be integer")
        if target < lyst[0] or target > lyst[-1]:
            return False
        if last > len(lyst) - 1:
            last = len(lyst) - 1
        if target > lyst[last]:
            first = last
            last += step
        elif target <= lyst[last]:
            possible_range = lyst[first: last+1]
            for value in possible_range:
                if isinstance(value, int) == False:
                    raise ValueError("List values must be integer")
                if value == target:
                    return True
            return False


def main():
    '''Creates lyst, sets targets, searches for targets via each algorithm and returns results '''
    lyst = create_lyst()

    target_values = [lyst[0], lyst[int(len(lyst)/2)], lyst[-1]]

    # searching for first value
    print("\nSearching for a number at the start of the array...")
    linear_start = perf_counter()
    linear_return = linear_search(lyst, target_values[0])
    linear_time = perf_counter() - linear_start
    print(
        f"\t linear_search() returned {linear_return} in {linear_time} seconds")

    binary_start = perf_counter()
    binary_return = recursive_binary_search(lyst, target_values[0])
    binary_time = perf_counter() - binary_start
    print(
        f"\t recursive_binary_search() returned {binary_return} in {binary_time} seconds")

    jump_start = perf_counter()
    jump_return = jump_search(lyst, target_values[0])
    jump_time = perf_counter() - jump_start
    print(f"\t jump_search() returned {jump_return} in {jump_time} seconds")

    # searching for mid value
    print("Searching for a number in the middle of the array...")
    linear_start = perf_counter()
    linear_return = linear_search(lyst, target_values[1])
    linear_time = perf_counter() - linear_start
    print(
        f"\t linear_search() returned {linear_return} in {linear_time} seconds")

    binary_start = perf_counter()
    binary_return = recursive_binary_search(lyst, target_values[1])
    binary_time = perf_counter() - binary_start
    print(
        f"\t recursive_binary_search() returned {binary_return} in {binary_time} seconds")

    jump_start = perf_counter()
    jump_return = jump_search(lyst, target_values[1])
    jump_time = perf_counter() - jump_start
    print(f"\t jump_search() returned {jump_return} in {jump_time} seconds")

    # searching for last value
    print("Searching for a number at the end of the array...")
    linear_start = perf_counter()
    linear_return = linear_search(lyst, target_values[2])
    linear_time = perf_counter() - linear_start
    print(
        f"\t linear_search() returned {linear_return} in {linear_time} seconds")

    binary_start = perf_counter()
    binary_return = recursive_binary_search(lyst, target_values[2])
    binary_time = perf_counter() - binary_start
    print(
        f"\t recursive_binary_search() returned {binary_return} in {binary_time} seconds")

    jump_start = perf_counter()
    jump_return = jump_search(lyst, target_values[2])
    jump_time = perf_counter() - jump_start
    print(f"\t jump_search() returned {jump_return} in {jump_time} seconds")

    # searching for missing value
    print("Searching for a number NOT in the array...")
    linear_start = perf_counter()
    linear_return = linear_search(lyst, -1)
    linear_time = perf_counter() - linear_start
    print(
        f"\t linear_search() returned {linear_return} in {linear_time} seconds")

    binary_start = perf_counter()
    binary_return = recursive_binary_search(lyst, -1)
    binary_time = perf_counter() - binary_start
    print(
        f"\t recursive_binary_search() returned {binary_return} in {binary_time} seconds")

    jump_start = perf_counter()
    jump_return = jump_search(lyst, -1)
    jump_time = perf_counter() - jump_start
    print(f"\t jump_search() returned {jump_return} in {jump_time} seconds")


if __name__ == "__main__":
    main()
