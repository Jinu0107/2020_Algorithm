# level : 1
# link : https://programmers.co.kr/learn/courses/30/lessons/12916
# title : 문자열 내 p와 y의 개수
# key : count() , lower()



def solution(s):
   return s.lower().count('p') == s.lower().count('y')



print(solution("PyyPppYyyP"))