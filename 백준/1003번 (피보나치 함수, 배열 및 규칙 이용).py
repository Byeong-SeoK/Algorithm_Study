N = int(input())

"""
입력 값 --> 0/1 등장 횟수
n = 0 --> (1,0)
n = 1 --> (0,1)
n = 2 --> (1,1)
n = 3 --> (1,2)
n = 4 --> (2,3)
이므로 항상 다음 값은 이전 값 2개를 더한 것과 동일하다.
"""
for i in range(0, N):
    number = int(input())
    fib = [[1, 0], [0, 1]]

    if(number == 0):
        print(fib[0][0], fib[0][1])
    elif(number == 1):
        print(fib[1][0], fib[1][1])
    else:
        index = 2
        while (index < number + 1):
            zero = fib[index - 1][0] + fib[index - 2][0]
            one = fib[index - 1][1] + fib[index - 2][1]
            fib.append([zero, one])
            index = index + 1

        print(fib[number][0], fib[number][1])
