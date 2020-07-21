def solution(phone_book):
    answer = True
    for i in phone_book:
        for j in phone_book:
            if i != j and i.startswith(j):
                return False
               
    
    return answer


print(solution(["119", "97674223", "1195524421"]))
