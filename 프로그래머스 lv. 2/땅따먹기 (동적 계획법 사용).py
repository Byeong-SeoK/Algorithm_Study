def solution(land):
    answer = 0
    N = len(land) #N행을 받는 변수
    
    SUM = [[0]*4 for i in range(0, N)]
    #각 행의 특정 열을 밟았을 때 나올 수 있는
    #각 경우의 합을 받는 배열이다.
    #이때 SUM 배열 선언을 SUM = [[0]*4]*len(land)로 하면
    #단순히 요소([0,0,0,0])만 복사하여(얕은 복사) 이어붙인
    #2차원 배열이 된다. 그래서 SUM[0][0]만을 수정해도
    #SUM[0][0]을 얕게 복사하여 받은 SUM[1][0], SUM[2][0]도
    #한번에 같이 수정된다. 그러므로 위와 같이 for문을 이용하여 선언해야한다.
    
    for j in range(0, 4):
        SUM[0][j] = land[0][j]
    
    for p in range(1, N): 
        #동적 계획법으로 최대값을 찾는다.
        #SUM[p-1][?]에는 SUM[p-1][?]까지 가는데 가장 최대 점수에 해당하는
        #값이 들어있다. 즉, SUM[p][?]에 대해서 가장 최대를 구하는 것은
        #SUM[p-1][?]에 land[p][?]를 더하는 것과 같다.
        
        SUM[p][0] = land[p][0] + max(SUM[p-1][1], SUM[p-1][2], SUM[p-1][3])
        SUM[p][1] = land[p][1] + max(SUM[p-1][0], SUM[p-1][2], SUM[p-1][3])
        SUM[p][2] = land[p][2] + max(SUM[p-1][0], SUM[p-1][1], SUM[p-1][3])
        SUM[p][3] = land[p][3] + max(SUM[p-1][0], SUM[p-1][1], SUM[p-1][2])
        
    answer = max(SUM[N-1])
        
    return answer


"""
다른 풀이(land 배열 하나만으로 풀이)

def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]
            #max(land[i -1][: j] + land[i - 1][j + 1:]) 이 뜻은 결국
            #i-1번째 배열의 모든 값들을 더한 값 중에서 가장 최대 값을 찾는다는 것이다.

    return max(land[-1])
"""
