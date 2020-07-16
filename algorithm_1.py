# level : 1
# link : https://programmers.co.kr/learn/courses/30/lessons/42576
# title : 완주하지 못한 선수
# key : counter



from collections import Counter

def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]

