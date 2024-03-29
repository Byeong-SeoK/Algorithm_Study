def solution(s):
    answer = []
    
    element = []
    #{}사이의 숫자만 받을 배열
    
    temp = [] #s의 각 튜플을 배열로 만들기 위한 임시 배열
    num = "" 
    #s의 튜플을 보면 111같은 숫자가 있는데 s는 string 타입이므로
    #for문으로 접근하면 1,1,1로 접근하게 되므로 
    #1+1+1로 111이 만들어지도록 해야한다. 
    
    for i in range(0, len(s)):
        if(s[i] == '{'):
            #string s에서 튜플의 시작점인 '{'는 필요가 없으므로 제외
            continue
        elif(s[i] == ',' and s[i-1] == '}'):
            #string s에서 튜플 간 구분자 역할을 하는 '},'는 필요가 없으므로 제외
            continue
        elif(s[i] == ',' and s[i-1] != '}'):
            #string s에서 ',' 앞이 '}'이 아닌 경우는 반드시 숫자인 경우이므로
            #temp 배열에 해당 숫자를 추가하도록 한다.
            temp.append(int(num))
            num = ""
            #숫자 하나를 완벽하게 만들었으므로 num을 다시 ""로 초기화 한다.
            
        elif(s[i] == '}'):
            if(i == len(s)-1):
                #s[i]가 '}'인데 해당 index가 len(s)-1이면 제일 끝의
                #'}'에 해당하므로 for문을 멈추도록 한다.
                break
            else:
                #s[i]가 '}'인데 해당 index가 len(s)-1인 아닌 경우에는
                #반드시 한 튜플의 끝을 의미하는 것이다.
                #그러므로 temp에 들어있던 한 튜플의 숫자들의 배열을
                #element배열에 추가하고 temp를 []로 초기화한다.
                #하지만 그 전에 ',3}'와 같은 경우이기도 하므로
                #num을 이용하여 만들어진 숫자를 temp에 추가하고
                #num을 ""으로 초기화 해야한다.
                temp.append(int(num))
                element.append(temp)
                temp = []
                num = ""
        else:
            #111 같은 숫자가 튜플 내에 존재할 수 있으므로
            #1+1+1과 같은 형태로 하나의 숫자로 string을 만들도록 해야한다.
            num = num+s[i]
            
    element.sort(key=len)
    #element 배열의 요소를 각 요소의 길이를 기준으로 정렬한다.
    
    for j in range(0, len(element)):
        for k in range(0, len(element[j])):
            if(element[j][k] not in answer):
                #해당 튜플의 값들이 배열에 없으면 그 튜플의 값들을 배열에 넣는다.               
                answer.append(element[j][k])
            else:
                #해당 튜플의 값이 배열에 있으면 건너뛴다.
                continue
    
    return answer
