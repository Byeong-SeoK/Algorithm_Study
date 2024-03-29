import math
from itertools import *
def solution(nums):
    answer = 0
    
    comb = list(combinations(nums, 3))
    #3개를 뽑아서 합산이므로 사실상 numsC3의 조합 형태이다.
    #(1,2,3) 이나 (3,2,1) 이나 합은 같기 때문
    case = [] #각 경우의 합의 값이 들어가는 배열
    for m in comb:
        Sum = 0
        for n in m:
            Sum = Sum+n
        m = Sum
        case.append(Sum)

    for i in range(0, len(case)):
        if(case[i] == 1):
            answer = answer+1
        elif(case[i] == 2):
            answer = answer+1
        elif(case[i] == 3):
            answer = answer+1
        else:
            find = False
            for j in range(2, math.floor(math.sqrt(case[i]))+1):
                #3이상의 수 들에 대해서는 각각의 제곱근값에 대해서
                #해당 제곱근까지의 값으로 나누어서 합성수인지 소수인지 판별한다.
                if(case[i]%j == 0):
                    find = False
                    case[i] = 0
                    break
                else:
                    find = True
            if(find):
                answer = answer+1
    
    return answer
