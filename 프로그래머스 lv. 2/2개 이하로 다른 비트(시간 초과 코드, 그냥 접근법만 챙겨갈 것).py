def solution(numbers):
    answer = []
    
    num = 0 #다른 비트의 개수가 2이하가 될 수를 받을 변수
    index = 0 #numbers 배열의 index 변수
    loop = 0 
    #numbers의 원소 한 개에 몇번 loop를 반복했는지 받는 변수
    #즉 numbers[index]에 +1을 총 몇 번하고 있는지 받는 변수이다.
    #이를 하는 이유는 while문 안에서 처음에 num = numbers[index]를 받기 때문
    
    while index != len(numbers):
        if(loop == 0): #처음에는 num애 numbers[index]값을 주고 거기에 +1을 한다.
            num = numbers[index]+1
        else: #이후부터는 num 자체에 +1을 계속 한다.
            num = num+1
            
        two_b = bin(num^numbers[index])
        #num과 numbers[index]를 XOR 연산을 하면 이 두 값 간에
        #1이 몇 개가 다른지 알 수 있다.
        #ex) 0111 XOR 1000 = 1111이 나온다.
        
        count = two_b.count('1') 
        #연산된 값에서 1의 개수가 몇개인지 센다.
        #이때 two_b는 string형 이므로 count 내장 함수를 이용  
        
        loop = loop+1
        
        if(count <= 2):
            answer.append(num)
            index = index+1
            loop = 0
        
    return answer


"""
1씩 더하는 것 말고 짝수일 때는 +1, 홀수 일때는 2^N의 값을 더하는 방식으로 더 나은 알고리즘 구현 가능
하지만 비트의 길이가 다를 경우를 해결해야하는 문제가 있다..
"""
