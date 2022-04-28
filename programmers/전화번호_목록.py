# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book): 
    phone_book = sorted(phone_book)
    
    for n1, n2 in zip(phone_book, phone_book[1:]):
        if n2.startswith(n1):        
            return False

    return True