# 369게임[2단계]
# 1. 1~50까지 반복을 한다.
# 2. 그 안에서 해당 숫자의 369게임의 결과를 출력한다.
# 예) 1 2 짝 4 5 짝 7 8 짝 10 11 12 짝 ...
i = 1
while i <= 50:
    j = 0
    if str(i).find("3") == -1 and str(i).find("6") == -1 and str(i).find("6") == -1 :
        j = 1
    if j == 1:
        print(i)
    else :
        print("짝")
    i +=1