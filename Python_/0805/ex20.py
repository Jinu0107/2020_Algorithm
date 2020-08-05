# 카카오 택시
# 1. 손님을 태워 목적지까지 이동하는 게임이다.
# 2. -10~10 사이의 랜덤 숫자 2개를 저장해 목적지로 설정한다.
# 3. 메뉴는 아래와 같다.
# 		1) 속도설정 : 1~3까지만 가능
# 		2) 방향설정 : 동(1)서(2)남(3)북(4)
# 		3) 이동하기 : 설정된 방향으로 설정된 속도만큼 이동
# 4. 거리 2칸 당 50원씩 추가되어 요금도 출력한다.
# 예) 1(50) 2(50) 3(100) 4(100) ...

# 목적지(destination)
import random

des_x = random.randint(-10,10)
des_y = random.randint(-10,10)

# 현재 위치
x = 0
y = 0

# 방향(direction)
direc = 0

# 속도
speed = 0

# 요금
fee = 0

# 얼마나 움직였는지
move = 0

run = True
while run:
    if(x == des_x and y == des_y):
        break
    print("=== 카카오 택시 ===")
    print("목적지 :", des_x, des_y)
    print("현위치 :", x, y)
    print("방  향 :", direc)
    print("속  도 :", speed)
    print("요  금 : " , fee)



    print("1.방향설정")
    print("2.속도설정")
    print("3.이동하기")

    choice = int(input("메뉴 선택 : "))
    if choice == 1:
        direc = int(input("방향 설정하기 동(1)서(2)남(3)북(4) : "))
        pass
    elif choice == 2:
        speed = int(input("속도 설적하기 : (1~3)"))
        pass
    elif choice == 3:
        if direc == 1:
            x += speed
        elif direc == 2: 
            x -= speed
        elif direc == 3:
            y -= speed
        elif direc == 4:
            y += speed
        move += speed
        fee += int(move/2) * 50
        move = move % 2
        pass
print("도착")
