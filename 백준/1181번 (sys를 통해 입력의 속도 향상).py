import sys
N = int(sys.stdin.readline())
#sys.stdin.readline()이 input()보다 훨씬 빠르게 입력된다.

word = []
for i in range(0, N):
    word.append(sys.stdin.readline().strip())
    #sys.stdin.readline()에는 "\n"이 있으므로 strip으로
    #"\n"이 string값에 같이 들어가지 못하도록 막는다.
word = list(set(word))
word.sort() #사전 순으로 먼저 word를 정렬
word.sort(key=len) 
#사전 순으로 정렬된 것을 내장함수 len, 즉 단어 길이를 기준으로 재정렬
#key=를 통해서 sort의 기준을 설정할 수 있다.

for j in range(0, len(word)):
    print(word[j])
