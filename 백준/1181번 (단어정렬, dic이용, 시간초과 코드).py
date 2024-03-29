N = int(input())

word = []
dic = {}
for i in range(0, N):
    temp = input()
    if(len(temp) in dic): #dic안에 해당 key값이 있으면 추가
        dic[len(temp)].append(temp)
    else: #dic안에 해당 key값이 없으면 배열을 만들고 추가
        dic[len(temp)] = []
        dic[len(temp)].append(temp)

    dic[len(temp)] = list(set(dic[len(temp)])) #각 key값에 대해서 중복된 value 값을 제거한다.
    dic[len(temp)].sort() #각 key값에 대해서 value의 배열을 오름차순으로 정렬한다.

num = max(dic) #dic에서 가장 큰 값의 key를 num에 넣는다.
for j in range(0, num+1):
    if(j in dic): #만약에 dic안에 4라는 key가 없으면 건너뛰고 있으면 word에 해당 배열을 연결하도록 한다.
        word = word+dic[j]

for p in range(0, len(word)):
    print(word[p])
