def solution(n):
    number = set(range(2, n+1))

    for i in range(2, n+1):
        if i in number:
            number -= set(range(i*2, n+1, i))

    return len(number)



print(solution(10))