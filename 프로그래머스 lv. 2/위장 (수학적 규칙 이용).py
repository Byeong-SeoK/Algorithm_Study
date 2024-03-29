def solution(clothes):
    answer = 0
    
    count = 0
    #만들 수 있는 의상 조합 수를 받는 변수
    
    type = {}
    #의상 종류별로 무엇이 있는지 받는 사전
    
    for i in range(0, len(clothes)):
        part = clothes[i][1]
        #어디에 착용하는지 받는 변수
        
        if(part in type):
            type[part].append(clothes[i][0])
        else:
            type[part] = []
            type[part].append(clothes[i][0])
    
    for j in type:
        count = count + len(type[j])
        #의상을 하나만 입는 경우는 사전의 각 배열의 길이의 합과 같다.
    
    if(len(type) == 1):
        #의상 종류가 1가지만 있는 경우
        #그 의상을 하나만 입는 경우만 존재할 수 있다.
        answer = count
    else:
        temp = 1
        #모든 경우의 수를 곱셈으로 구하기 위해 임시로 받는 변수
        
        for k in type:
            temp = temp * (len(type[k])+1)
        answer = temp-1
        #모든 경우의 수는 예를 들어서 아래와 같이
        #의상이 [옷1, 옷2, 옷3] / [옷4, 옷5]
        #이렇게 존재할 때 총 경우의 수는
        #[아무것도 입지 않기, 옷1, 옷2, 옷3] * [아무것도 입지 않기, 옷4, 옷5]를
        #한 다음에 (아무것도 입지 않기 * 아무것도 입지 않기) 이 1가지 경우만
        #곱셈의 결과에서 빼면 된다.
        
    return answer
