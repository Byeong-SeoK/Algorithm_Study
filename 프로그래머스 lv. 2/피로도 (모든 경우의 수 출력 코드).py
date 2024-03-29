def solution(k, dungeons):
    answer = -1
    
    if(len(dungeons) == 1): #던전이 하나인 상황
        if(k < dungeons[0][0]): #최소 필요 피로도가 현재 피로도보다 큰 경우
            answer = 0
        else:
            answer = 1
    else:
        case = [dungeons[:]] #첫번째 case 묶음
    
        c = [0] * len(dungeons)
        i = 0
        while i < len(dungeons): #순서를 섞기 위한 반복문
            if c[i] < i:
                if i % 2 == 0:
                    dungeons[0], dungeons[i] = dungeons[i], dungeons[0]
                    #파이썬에서 다중 할당은 먼저 오른쪽에 해당하는 것에 대해 각각의 값을 준다. 
                    #즉 만약 여기서 dungeons[i] = a이고 dungeons[0] = b이면 위 식은
                    #dungeons[0], dungeons[i] = a, b 형태가 되고
                    #이는 각각을 dungeons[0] = a, dungeons[i] = b가 된다.
                else:
                    dungeons[c[i]], dungeons[i] = dungeons[i], dungeons[c[i]]
                case.append(dungeons[:]) #순서를 섞은 것을 배열에 저장
                c[i] = c[i]+1
                i = 0
            else:
                c[i] = 0
                i = i+1
    #print(case)
    
    way = [] #각 방법에 따른 돌 수 있는 던전수를 저장한 배열
    for m in case:
        number = 0 #각 순서에 대해 돌 수 있는 던전수
        life = k #체력을 받는 변수(k의 immutable을 위함)
        for n in m:
            if(life > n[0]): #남은 피로도 > 최소 피로도
                life = life-n[1]
                number = number+1
            elif(life == n[0]): #남은 피로도 == 최소 피로도
                life = life-n[1]
                number = number+1
            else: #남은 피로도 < 최소 피로도
                break
        way.append(number)
    
    way.sort(reverse=True)
    
    answer = way[0]
            
    return answer
