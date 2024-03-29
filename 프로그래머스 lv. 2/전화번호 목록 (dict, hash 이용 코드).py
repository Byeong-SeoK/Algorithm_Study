def solution(phone_book):
    answer = True
    
    num_hash = {} #phone_book의 각 번호를 넣을 Hash이다.
    
    for i in phone_book: #hash에 값을 넣는다.
        num_hash[i] = 1
    
    for phone_number in phone_book: #phone_book의 값을 하나씩 접근해 나간다.
        prefix = "" #접두사를 받는 변수
        
        for number in phone_number: #phone_number의 각각의 char를 number로 받는다.
            prefix = prefix + number
        
            if prefix in num_hash and prefix != phone_number:
                #prefix가 num_hash에 in이라는 조건을 만족하면 False이다.
                #prefix=119, phone_number=119인 경우는 해당사항이 없으므로 != 조건을 추가
                
                answer = False
                return answer
    
    return answer
