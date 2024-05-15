#!/usr/bin/env python

# S = "10001101"


# def solution(S):
#     S_list = list(S)
#     i = 0
#     while i < len(S_list) - 1:
#         if S_list[i] != S_list[i + 1]:
#             S_list.pop(i)
#             S_list.pop(i)
#         else:
#             i += 1
#     answer = len(S_list)
#     print(S_list)
#     return answer


# print(solution(S))

# def solution(S):
#     stack = []
#     for i in S :
#         if stack and stack[-1] != i :
#             stack.pop()
#         else :
#             stack.append(i)
#     return len(stack)

print(("11110000"))


def solution(S):
    S_list = list(S)
    i = 0
    while i < len(S_list) - 1:
        if S_list[i] != S_list[i + 1]:  # 붙어있는 문자가 서로 다를 때
            print("i_before =", i)
            S_list.pop(i)  # 현재 문자를 제거
            print("S_list_1 =", S_list)
            S_list.pop(i)  # 다음 문자를 제거 (현재 문자를 제거했으므로 인덱스가 당겨짐)
            print("S_list_2 =", S_list)
            #     i = max(0, i - 1)  # 인덱스를 하나 앞으로 당김 (다음 문자가 제거되었으므로)
            i = 0
            print("i_after =", i)
        else:
            i += 1
            print("i_else =", i)
    answer = len(S_list)  # 리스트를 다시 문자열로 변환
    return answer


print(solution("11110000"))  # 출력: "101"
