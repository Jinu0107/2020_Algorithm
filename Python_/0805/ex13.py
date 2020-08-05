import random

 
comleft = random.randint(0,2)
comright = random.randint(0,2)

r = random.randint(1,2)
com = 0
if r == 1:
    com = comleft
else :
    com = comright


print(com)
meleft = int(input("meleft ==> 0) 가위 , 1) 바위 , 2) 보"))
meright = int(input("meright ==> 0) 가위 , 1) 바위 , 2) 보"))

me = int(input("1) 왼손 , 2) 오른손"))

if me == 1:
    me = meleft
else :
    me = meright
result = ""
if me == 0:
    if com == 0:
        result = "비김"
    elif com == 1:
        result = "짐"
    else :
        result = "이김"
elif me == 1:
    if com == 0:
        result = "이김"
    elif com == 1:
        result = "비김"
    else :
        result = "짐"
elif me == 2:
    if com == 0:
        result = "짐"
    elif com == 1:
        result = "이김"
    else :
        result = "비김"
print(result)


    


    

