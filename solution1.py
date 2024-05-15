#!/usr/bin/env python

strs = ["abcaefg", "abcdefg", "abcdhfg"]
print("l_strs", len(strs))


def solution(strs):
    result = ""
    if len(strs) == 0:  # for when the list is empty
        return ""
    elif len(strs) == 1:  # for when the list has one element
        return strs[0]
    for i in range(len(strs[0])):
        print("i = ", i)
        prefix = strs[0][i]
        print("prefix = ", prefix)
        for c in range(1, len(strs)):
            print("c = ", c)
            print("i = ", i)
            print("strs[c][i] = ", strs[c][i])
            if i >= len(strs[c]) or strs[c][i] != prefix:
                return result
        result += prefix
        print("result = ", result)
    return result


solution(strs)
