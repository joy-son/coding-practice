#!/usr/bin/env python

arr = [5, 3, 9, 13]
n = 7


# def solution(arr, n):
#     num_set = set()
#     print("num_set =", num_set)
#     print("set =", set())
#     for i in arr:
#         result = n - i
#         print("i =", i)
#         print("result =", result)
#         if result in num_set:
#             return True
#         num_set.add(i)
#         print("result =", num_set)
#     return False


def solution(arr, n):
    for i in arr:
        print("i =", i)
        result = n - i
        print("result =", result)
        if result in arr:
            return True
    return False


print(solution(arr, n))
