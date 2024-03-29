def solution(numbers):
    answer = []
    
    num = 0 #다른 비트의 개수가 2이하가 될 수를 받을 변수
    index = 0 #numbers 배열의 index 변수
    loop = 0 
    #numbers의 원소 한 개에 몇번 loop를 반복했는지 받는 변수
    #즉 numbers[index]에 +1을 총 몇 번하고 있는지 받는 변수이다.
    #이를 하는 이유는 while문 안에서 처음에 num = numbers[index]를 받기 때문
    
    while index != len(numbers):
        if(numbers[index] % 2 == 0): #짝수일 때는 항상 +1을 해주면 된다.
            answer.append(numbers[index]+1)
            index = index+1
        else:
            b_num = format(numbers[index], 'b')
            #0b를 지운 2진수로 변환하는 것이다.
            
            two_b = [] #각 비트를 각 원소로 받는 배열, string은 위치 변경이 안되기 때문
            z_pos = 0 #가장 마지막 0인 비트의 자리 값을 받는 변수
            o_pos = 0 #가장 마지막 0인 비트의 바로 옆의 1인 비트의 자리 값을 받는 변수
            
            if(b_num.count('1') == len(b_num)):
                #111인 경우 1011이 되기 위해서 111을 0111로 만들어주어야 한다.
                #이런 경우 반드시 1의 개수가 string 전체 길이와 동일한 점을 이용한다.
                b_num = '0' + b_num
            
            for i in range(0, len(b_num)):#z_pos와 o_pos를 찾는 과정이다.
                two_b.append(b_num[i])
                if(b_num[i] == '0'):
                    z_pos = i
                    
                    if(i != len(b_num)-1):
                        #o_pos는 반드시 z_pos옆에 있으므로
                        #i가 마지막 index가 되기 전까지 o_pos는 i+1이 된다.
                        o_pos = i+1
            
            temp = two_b[z_pos]
            two_b[z_pos] = two_b[o_pos]
            two_b[o_pos] = temp
            #0의 위치와 1의 위치를 바꾸어준다.
            #즉, 1011은 1101이 나와야하는데 이때 2번째의 0과 3번째의 1의
            #위치를 서로 바꾸어준 것과 동일하다.
            
            result = ''
            for j in range(0, len(two_b)):
                result = result + two_b[j]
                        
            answer.append(int(result, 2))
            index = index+1
        
    return answer
