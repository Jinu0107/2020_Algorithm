# Up & Down 게임[2단계]
# 1. 정답을 맞추면 게임은 종료된다.
# 2. 100점부터 시작해 오답을 입력할 때마다 5점씩 차감된다.
# 3. 게임 종료 후, 점수를 출력한다.
import random


r = random.randint(1 , 100)

score = 100
while True:
    me = int(input("입력해보세요 : "))
    if me == r :
        break
    elif me > r :
        print("Down")
    else :
        print("Up")
    score -= 5

print(score , "점")