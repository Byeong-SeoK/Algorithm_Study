def solution(line):
    answer = []
    
    meet = [] #교점 중 정수형 교점 (x, y)를 가지고 있는 배열
    x_max = -int(1e15)
    x_min = int(1e15)
    y_max = -int(1e15)
    y_min = int(1e15)
    #max를 -int(1e15)로 min를 int(1e15)로 두는 이유는 0이나 -1 같은 범위 내의
    #임의의 정수로 값을 두면 아래 max, min 값 갱신 과정에서 해당 값과 같은 경우 
    #갱신이 되지 않게 된다. .과 *을 찍는 배열의 크기가 달라지게 된다.
    
    for i in range(0, len(line)):
        A = line[i][0] #첫번째 x항의 계수
        B = line[i][1] #첫번째 y항의 계수
        E = line[i][2] #첫번째 상수항
        
        for j in range(i+1, len(line)): #i번째의 함수는 포함할 필요X            
            C = line[j][0] #두번째 x항의 계수
            D = line[j][1] #두번째 y항의 계수
            F = line[j][2] #두번째 상수항
            
            parallel = A*D - B*C
            
            if(parallel == 0):
                continue
            else:
                num1 = B*F-E*D
                num2 = E*C-A*F
                
                x = num1/parallel
                y = num2/parallel
                
                if(x - int(x) == 0 and y - int(y) == 0):
                    #3.0 - int(3.0) --> 3.0 - 3 = 0임을 활용하여
                    #x, y가 각각 소수인지 아니면 정수인지 확인한다.
                    meet.append([int(x), int(y)])
                    
                    #아래의 4가지 조건문은 각각 x좌표의 최대 최소값
                    #y좌표의 최대 최소값을 찾는 과정이다.
                    if(x_max < x):
                        x_max = int(x)
                    
                    if(x_min > x):
                        x_min = int(x)
                    
                    if(y_max < y):
                        y_max = int(y)
                        
                    if(y_min > y):
                        y_min = int(y)
    
    x_length = x_max-x_min+1 #x축 해당 범위내의 x좌표의 개수
    y_length = y_max-y_min+1 #y축 해당 범위 내의 y좌표의 개수
    #각각에 1을 더한 이유는 (0,0)을 더한 것이다.
    
    point = [] #미리 점을 다 찍어놓은 임시 배열
    for p in range(0, y_length):
        point.append(["."]*x_length)
        
    for xpos, ypos in meet:
        #격자판의 제일 왼쪽 위가 배열상의 [0][0]에 해당
        #그러므로 TC1의 경우 제일 오른쪽 아래가 [8][8]에 해당하게 되고
        #TC1의 교점 (-4,-4)는 [8][0]이 되게 된다.
        #2차원 배열에서 앞의 []는 y축 뒤의 []는 x축에 해당한다.
        if(x_min < 0):
            xpos = xpos + abs(x_min)
            #(-4,-4)을 [8][0]로 만들어야 하므로 -4 + |-4|을 한다.
        else:
            xpos = xpos - x_min
            #(4, 1)을 [3][8]으로 만들어야 하므로 4 - (-4)를 한다.
        
        if(y_min < 0):
            ypos = ypos + abs(y_min)
            #(0, 4)을 [0][4]으로 만들어야 하므로 0 + |-4|를 한다.
        else:
            ypos = ypos - y_min
            #(4, 1)을 [3][8]으로 만들어야 하므로 1 - (-4)를 한다.
            
        point[ypos][xpos] = "*"
        #함수에서 (x,y)인 것을 배열로 표현할 때는 [y][x]로 나타내게 된다.
        
    #print(point)
    #point를 출력해보면 알 수 있지만 거꾸로 출력이 된다.
    #2차원 좌표계에서는 왼쪽이 -값, 오른쪽이 +값이라는 점은 동일하지만,
    #일반 행렬에서 위로 갈수록 작은 값이고 아래로 갈수록 큰 값인 것과 반대로 
    #2차원 좌표계에서는 위로 갈수록 큰 값, 아래로 갈 수록 작은 값이다.
    #그래서 거꾸로 담아야한다.
    
    for a in range(len(point)-1, -1, -1):
        answer.append(''.join(point[a]))
        
    return answer
