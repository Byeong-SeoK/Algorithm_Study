def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for i in range(len(arr1))]
    # arr2를 곱하기 쉽도록 시계 방향으로 90도 돌림 
    turn_arr2 = [[arr2[i][j] for i in range(len(arr2))] for j in range(len(arr2[0]))]
    #위 식은 행렬의 내적할 때 형태인 (가로) * (세로) 형태로 만들기 위함이다.
    #그래서 가로, 가로 형태의 배열 중 하나를 세로 형태로 바꾸어야 한다.

    for i in range(len(arr1)):
        for j in range(len(turn_arr2)):
            arg = 0  # answer[i][j]에 들어갈 값
            for x, y in zip(arr1[i], turn_arr2[j]): # 같은 인덱스의 값끼리 매칭해줌
		#zip함수를 사용하면 x, y에 각각 서로 다른 값을 for문 돌 때 마다 하나씩 넣을 수 있다.
                arg += x * y # 값들을 곱해서 arg에 더해줌 
            answer[i][j] = arg 

    print(answer)
    return answer
