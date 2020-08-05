# 반복문 while
# 반복의 조건 3가지
# 1) 초기식
# 2) 조건식
# 3) 증감식

# 구조
# 초기식
# while 조건식:
#   조건식이 참일 동안 실행할 문장
#   증감식

# 예) 1부터 5까지 출력
i = 1
while i <= 5:
    print(i)
    i = i + 1



# 영수증 출력[2단계]
# 1. 5번 주문을 받는다.
# 2. 주문이 끝난 후, 돈을 입력받는다.
# 3. 각 메뉴별 주문수량과 총금액을 출력한다. 
# 예)
# 메뉴 선택 : 1
# 메뉴 선택 : 1
# 메뉴 선택 : 2
# 메뉴 선택 : 2
# 메뉴 선택 : 3
# 총 금액 = 31300원
# 현금 입력 : 32000
# === 롯데리아 영수증 ===
# 1. 불고기 버거 : 2개
# 2. 새우    버거 : 2개
# 3. 콜         라 : 1개
# 4. 총   금   액 : 31300원
# 5. 잔         돈 : 700원

price1 = 8700
price2 = 6200
price3 = 1500

print("=== 롯데리아 ===")
print("1.불고기 버거 :", price1)
print("2.새우   버거 :", price2)
print("3.콜       라 :", price3)

pricearr = [8700 , 6200 , 1500]
strarr = ["불고기 버거" , "새우   버거" , "콜       라 "]
arr = [0, 0 ,0]

i =1
while i <= 5:
    idx = int(input("수 입력 : "))-1
    arr[idx] += 1
    i = i+1
total = 0

for i in range(0,len(arr)):
    total += pricearr[i]*arr[i]
print("총 금액 = " , total , "원")
price = int(input("현금 입력 : "))
if total > price:
    print("돈이 부족합니다")
else :
    print("== 롯데리아 영수증 ==")
    for i in range(0,len(arr)):
        if arr[i] != 0:
            print(i+1 , "." , strarr[i] , " : " , arr[i] , "개")
    print("총   금   액 : " , total)
    print("잔        돈 : " , price-total)
    
    
     
        
