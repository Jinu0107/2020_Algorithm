# 가운데 숫자 맞추기 게임
# 1. 150~250 사이의 랜덤 숫자 저장
# 2. 랜덤 숫자의 가운데 숫자를 맞추는 게임이다.
# 예)
# 		249		: 4

import random

r =  str(random.randint(150 , 250))

print(r)
m = input("중간값을 입력하세요")

if r.find(m) == 1:
    print("정답")
else :
    print("오답")

