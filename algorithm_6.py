# level : 1
# url : https://programmers.co.kr/learn/courses/30/lessons/12912
# title : 두 정수 사이의 합


def solution(a, b):
    answer = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b, a+1):
            answer += i
    else:
        for i in range(a, b+1):
            answer += i

    return answer