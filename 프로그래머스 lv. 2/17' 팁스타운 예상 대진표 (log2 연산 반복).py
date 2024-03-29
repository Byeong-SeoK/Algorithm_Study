def solution(n,a,b):
    answer = 0
    
    if(a % 2 == 0 and a-b == 1):
        answer = 1
    elif(b % 2 == 0 and b-a == 1):
        answer = 1
        
    #위 2가지 경우는 각각 A: 4, B: 3
    #A: 3, B: 4인 경우이다.
    #이 경우 항상 첫번째 만나게 되므로
    #answer = 1이 된다.
    
    else:
        count = 1
        #경기 몇 번 해야하는지 받는 변수
        
        while True:
            if(b%2 == 0 and b-a == 1):
                answer = count
                break
            
            if(a%2 == 0 and a-b == 1):
                answer = count
                break
                
            #위의 2개의 if문은 A, B가 맞붙게 되는 경우이므로
            #더 이상 경기할 필요가 없으므로 반복문을 종료시킨다.
            
            if(a%2 == 0):
                #A가 4번인 경우 다음 경기에서의
                #A는 2번이 된다. 그러므로 //를 적용
                a = a//2
            else:
                #A가 7번인 경우 다음 경기에서의
                #A는 4번이 된다. 그러므로 //를 적용한 다음
                #그 값에 +1을 해주어야 한다.
                a = a//2+1
            
            if(b%2 == 0):
                b = b//2
            else:
                b = b//2+1
            
            
            n = n // 2
            #사람 수는 항상 절반으로 줄어든다.
            
            count = count+1
            #경기 수를 한번 더 늘린다.

    return answer
