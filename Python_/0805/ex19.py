# 랜덤학생
# 1. 10회 반복을 한다.
# 2. 1~100 사이의 랜덤 숫자를 저장한다.(학생의 성적)
# 3. 성적이 60점 이상이면 합격생이다.
# ---------------------------------------
# . 전교생(10명)의 총점과 평균을 출력한다.
# . 합격자 수를 출력한다.
# . 1등 학생의 번호와 성적을 출력한다.
import random

i = 1
total = 0
top =[0 , 0]
pass_cnt = 0
while i <= 10:
    score = random.randint(1,100)
    if score >= 60 :
        pass_cnt +=1
        if top[0] <= score :
            top[0] = score
            top[1] = i
    total += score

    i += 1 

print("전교생 총점 : " , total)
print("평균 : " , total/10 )
print("합격자 수 : " , pass_cnt)
print("1등 성적 번호 : " , top[0] , " , " , top[1])