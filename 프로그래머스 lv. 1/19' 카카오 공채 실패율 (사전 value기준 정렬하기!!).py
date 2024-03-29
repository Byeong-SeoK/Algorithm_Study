def solution(N, stages):
    answer = []
    user = len(stages)
    #실패율을 구하려는 스테이지 범위 내에 있는 유저 수
    #유저 수가 사실상 stages 배열의 길이와 같다.
    
    stages.sort() #rate가 오름차순이 될 수 있도록 stages를 sort한다.
    rate = {} 
    #stages를 통해 구하는 실패율 사전
    #이후 fault라는 사전을 통해 쓸데없는 스테이지의 실패율은 버리고
    #필요로하는 실패율만 담도록 하기 위한 임시 사전에 가깝다.
    for i in range(0, user):
        if(stages[i] in rate):
            rate[stages[i]] = rate[stages[i]]+1
        else:
            rate[stages[i]] = 1
    
    for j in rate:
        temp = rate[j]
        #rate[j]값이 소수로 바뀔 것이므로 user를 변동시킬 때 필요한
        #rate[j]값을 미리 temp에 따로 빼놓는다.
        rate[j] = rate[j] / user
        user = user - temp 
        #해당 스테이지를 못 깬 사람은 다음 스테이지 실패율 계산에서의
        #모집단에서 제외되어야 한다. 왜냐하면 해당 스테이지에 가지도 못했기 때문
    #print(rate)
    
    fault = {}
    #TC1을 보면 N은 5까지인데 stages 배열에 5는 없고 6은 있다.
    #하지만 우리는 6은 필요 없으므로 우리가 실제로 필요로 하는 실패율만 모아놓은
    #사전 fault를 만들고 1부터 N 스테이지까지의 실패율을 담는다.
    #이때 rate에 없던 스테이지에 대한 실패율은 반드시 0이다.
    
    for p in range(1, N+1):
        if(p not in rate):
            fault[p] = 0.0
        else:
            fault[p] = rate[p]
    #print(fault)
    
    fault = sorted(fault.items(), reverse= True, key = lambda item: item[1])
    #위 코드는 사전을 value기준으로 내림차순으로 정렬하는 코드이다.
    #lambda 함수를 이용하여 키(key)로 사용할 기준이 값(value), 
    #즉 item[1] 이라고 지정을 해주면 된다. (키는 item[0], 값은 item[1] 로 indexing)
    #그리고 내림차순으로 정렬하므로 reverse= True라는 옵션을 넣으면 된다.
    #이때 리턴 값은 배열인데 각 요소가 튜플의 형태이다.
    #print(fault)
    
    for q in fault:
        answer.append(q[0])
        
    return answer
