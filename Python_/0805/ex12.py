# 지하철 요금 계산
#  1. 이용할 정거장 수를 입력받는다.
#  2. 다음과 같이 정거장 수에 따라 요금이 정산된다.
#  3. 요금표
#  1) 1~5	: 500원
#  2) 6~10	: 600원
#  3) 11,12 : 650원
#  4) 13,14 : 700원
#  5) 15,16 : 750원


cnt = int(input("정거장 수를 입력하세요"))
price = 0
if cnt <= 5:
    price += 500
elif cnt <= 10:
    price += 600
elif cnt <= 12:
    price += 650
elif cnt <= 14:
    price += 700
elif cnt <= 16:
    price += 750

print(price)


