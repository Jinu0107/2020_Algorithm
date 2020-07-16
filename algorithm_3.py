# level : 1
# link : https://programmers.co.kr/learn/courses/30/lessons/42748
# title : K번째 수
# key : sort , sorted()
# return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))






def solution(array, commands):
    answer = [] 
    for i in commands:
        arr = array[i[0]-1:i[1]]
        arr.sort()
        answer.append(arr[i[2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))