import sys
N, M = map(int, sys.stdin.readline().split())
chess = [] #초기 체스판을 담는 배열

for i in range(0, N): #체스판을 구현하는 과정
    chess.append(sys.stdin.readline())
    
"""
(0,0)이 B이면 (0,1) & (1,0)은 W가 되어야 한다. 혹은 그 반대가 되어야한다.
즉 행과 열의 index 합이 짝수인 것과 홀수인 것은 서로 다른 값을 가져야한다.
그래서 (0,0)이 어떤 색깔 값을 갖든 이후의 행과 열의 index 합이 짝수인 것과 동일해야한다.
"""

count = [] #각 case별로 몇 개의 블록을 색칠해야하는지 저장하는 배열이다.
"""
if (11,11) 인 경우
8x8로 가로로 자를 수 있는 경우는 총 4가지이다.
가로: /BBBBBBBB/BBB, B/BBBBBBBB/BB, BB/BBBBBBBB/B, BBB/BBBBBBBB/
마찬가지로 세로로 자를 수 있는 경우는 총 4가지이다.
세로: /BBBBBBBB/BBB, B/BBBBBBBB/BB, BB/BBBBBBBB/B, BBB/BBBBBBBB/
따라서 항상 입력받은 가로 세로 값에서 7을 뺀 값을 적용하여 for문을 돌리면 된다.
"""
for a in range(0, N-7):
    for b in range(0, M-7):
        index1 = 0 #'W'로 시작할 경우 다시 색칠해야하는 것 count
        index2 = 0 #'B'로 시작할 경우 다시 색칠해야하는 것 count
        
        for i in range(a, a+8): #행의 시작점 a를 기준으로 8칸씩 체크한다.
            for j in range(b, b+8): #열의 시작점 b를 기준으로 8칸씩 체크한다.
                if (i+j) % 2 == 0: #인덱스의 합이 짝수인 경우
                    if chess[i][j] != 'W': 
                        #시작점이 W인데 짝수가 B이면 다시 칠해야하므로 index1에 +1을 한다.
                        index1 += 1
                        
                    if chess[i][j] != 'B':
                        #시작점이 B인데 짝수가 W이면 다시 칠해야하므로 index2에 +1을 한다.
                        index2 += 1
                        
                else: #인덱스의 합이 홀수인 경우
                    if chess[i][j] != 'B':
                        #시작점이 B인데 홀수가 W이면 다시 칠해야하므로 index1에 +1을 한다.
                        index1 += 1
                        
                    if chess[i][j] != 'W':
                        #시작점이 W인데 짝수가 B이면 다시 칠해야하므로 index2에 +1을 한다.
                        index2 += 1
                        
        count.append(min(index1, index2))
        #W인 것을 다시 칠하는 경우와 B인 것을 다시 칠하는 경우 중 더 작은 것을 count에 넣는다. 

print(min(count))
#count에 모든 경우에 대한 값이 다 들어있고 그 중에서 최솟값을 출력하면 된다.
