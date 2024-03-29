def solution(arr1, arr2):
    answer = [[] for i in range(len(arr1))]
    for i, a in enumerate(arr1): #enumerate함수를 통해서 인덱스 값과 그 인덱스의 value가 각각 i, a에 들어감
	#여기서 arr1[i]는 2차원 배열의 각 가로줄 값이 a에 들어가고 a는 배열을 받는 변수가 된다.
        
        for b in zip(*arr2): #2차원 배열 세로 값 출력
            arg = 0
            for x, y in zip(a, b):
                arg += x * y #x에는 arr1의 가로줄 값 y에는 arr2의 세로줄 값이 들어가있고 이 식은 내적에 해당한다.
            answer[i] += [arg]#내적된 값(배열)을 answer에 추가한다.
    return answer


======= 부가 설명 =======
>>> for entry in enumerate(['A', 'B', 'C']):
...     print(entry)
...
(0, 'A')
(1, 'B')
(2, 'C')

enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 터플(tuple)을 만들어줍니다. 
따라서 인덱스와 원소를 각각 다른 변수에 할당하고 싶다면 인자 풀기(unpacking)를 해줘야 합니다.

>>> for i, letter in enumerate(['A', 'B', 'C']):
...     print(i, letter)
...
0 A
1 B
2 C


+알파
iter함수를 배열에 취하고 next함수를 적용하면 배열의 각 문자들이 출력된다.
>>> iter_letters = iter(['A', 'B', 'C'])
>>> next(iter_letters)
'A'
>>> next(iter_letters)
'B'
>>> next(iter_letters)
'C'


 for b in zip(*arr2): 에 대해
ex)
alist = [[1,1,1], [2,2,2], [3,3,3]] 일 때 for문에 zip(*alist)를 적용하면

for i in map(list, zip(*alist)):
    print(i)
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]

2차원 배열의 세로 줄의 값이 배열 형태로 묶여서 출력된다.
