#[무조건 배열(리스트로만 사용해서 구현)]

# 숫자이동[2단계]
# 1. 숫자2는 캐릭터이다.
# 2. 숫자1을 입력하면, 캐릭터가 왼쪽으로
# 	 숫자2를 입력하면, 캐릭터가 오른쪽으로 이동한다.
# 3. 단, 좌우 끝에 도달했을 때, 예외처리를 해야한다.
# 4. 숫자 1은 벽이다. 벽을 만나면 이동할 수 없다.
# 5. 단, 숫자3을 입력하면, 벽을 격파할 수 있다.

game = [0, 0, 1, 0, 2, 0, 0, 1, 0]

while False:
    print(game)
    num = int(input("수를 입력하세요 (1)왼쪽 , (2)오른쪽 , (3)벽부수기 : "))
    myIdx = game.index(2)
    if num == 1:
        if game[myIdx-1] != 1:
            game[myIdx] = 0
            if myIdx -1 < 0:
                myIdx = len(game)
            
            game[myIdx -1] = 2
        else:
            print("벽이 있습니다")
    elif num == 2:
        
        if game[myIdx+1] != 1 and myIdx+1 != 9:
            game[myIdx] = 0
            game[myIdx + 1] = 2
            if myIdx + 1 > len(game)-1:
                myIdx = -1    
        else:
            print("벽이 있습니다.")
    elif num == 3:
        game[myIdx + 1] = 0
        game[myIdx - 1] = 0
    



#===============================

# 중복숫자 금지[2단계]
# 1. arr배열에 1~10 사이의 랜덤 숫자 5개를 저장한다.
# 2. 단 중복되는 숫자가 없어야 한다.
import random

nums = [0 for i in range(5)]
i = 0
while i < 5:
    r = random.randint(1,10)
    if r not in nums:
        nums[i] = r
    else:
        i = i -1
        continue 
    i += 1
#print(nums)

#=================================

# 숫자 야구 게임
# 1. me에 1~9 사이의 숫자 3개를 저장
#    (단, 중복되는 숫자는 저장 불가)
# 2. com과 me를 비교해 정답을 맞출 때까지 반복
# 3. 숫자와 자리가 같으면 		strike += 1
#    숫자만 같고 자리가 틀리면 	ball += 1
# 예)
# 정답 : 1 7 3
# 3 1 5		: 2b
# 1 5 6		: 1s
# ...
import random
com = nums[0:3]
strike = 0
ball = 0
me = []
while True :
    while len(me) != 3:
        num = int(input("입력하세요 : "))
        if  num not in me:
            me.append(num)
    
    for i in range(0 , len(com)):
        if me[i] in com:
            if me[i] == com[i]:
                strike += 1        
            else:
                ball += 1
    if(strike == 3):
        print("정답입니다")
        break
    print(strike , "스크라이크 " , ball , "볼")
    strike = 0
    ball = 0
    me = []