
def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] =0

                if len(stack) > 1:
                    if(stack[-1] == stack[-2]):
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2
                break
    return answer



print(solution([[0,0,0,0,0],
          [0,0,1,0,3],
          [0,2,5,0,1],
          [4,2,4,4,2],
          [3,5,1,3,1]]	, [1,5,3,5,1,2,1,4]))


arr = [1,2,3,4,5,6,7]
print(arr[-1] , arr[-2])
arr.pop()
arr.pop()
print(arr)