def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow+1): #yellow의 약수를 찾는다.
        if(yellow % i == 0):
            x = i #x는 yellow 격자 부분의 세로 길이
            y = int(yellow//i) #y는  yellow 격자 부분의 가로 길이
            
            #세로 길이를 먼저 선언한 이유: 가로가 세로보다 더 길기 때문
            #for문에 의해 i가 작은 값 부터 시작하므로 항상 x가 y보다 작은 값을 갖는다.
            
            size = (x+2)*(y+2) - x*y 
            #brown 격자의 가로길이와 세로길이는 항상 yellow격자의 가로길이+2, 세로길이+2 이다.
            #size는 brown격자 개수의 변수로 카펫의 격자 전체 개수에서 yellow 격자 개수를 뺀다.
            
            if(size == brown):
                answer.append(y+2) #가로를 먼저 배열에 담는다.
                answer.append(x+2)
                break #값을 찾았으므로 for문 탈출
        
    return answer
