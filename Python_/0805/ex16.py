
# 베스킨라빈스31
# 1. p1과 p2가 번갈아가면서 1~3을 입력한다.
# 2. br은 p1과 p2의 입력값을 누적해서 저장한다.
# 3. br이 31을 넘으면 게임은 종료된다. (넘긴쪽이 패배)
# 4. 승리자를 출력한다.
# 
# 예) 
# 1턴 : p1(2)	br(2)
# 2턴 : p2(1)	br(3)
# 3턴 : p1(3)	br(6)

p1 = 0
p2 = 0

br = 0
turn = 0

while br < 31:
    if turn == 0:
        p1 = int(input("수 입력 : "))
        br += p1
        turn = 1
    else :
        p2 = int(input("수 입력 : "))
        br += p2
        turn = 0
    print(br)

print("p" , turn+1)
    
    
        