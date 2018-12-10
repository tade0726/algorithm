"""
Author : Ted
Date   : 2018-12-10 20:37
Email  : zp913913@gmail.com
"""
import random

# 二分法查找

def binary_search(list, item):

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid


def binary_search2(l: list, item):

    high = len(l) - 1
    low = 0

    while low <= high:

        mid = int((high + low) / 2)
        guess = l[mid]

        if item > guess:
           low = mid + 1
        elif item < guess:
            high = mid - 1
        else:
            return mid
    return


def test_function(func):
    binary_search = func
    print(f"function name: {binary_search.__name__}")
    a = random.choices(range(100), k=8)
    target = random.choice(range(100))
    a.append(target)
    a = sorted(list(set(a)))

    print(f"target: {target}, list: {a}")
    print(f"binary return:", binary_search(a, target))
    print(f"actual result: {a.index(target)}")
    print()


if __name__ == "__main__":
    test_function(binary_search)
    test_function(binary_search2)
