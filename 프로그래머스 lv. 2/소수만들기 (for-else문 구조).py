def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
	#이 for-else문은 안쪽 for문이 돌다가 break에 걸려 for문을 탈출하지 못하였을 때 else문이 호출된다.
	#그래서 else문에 소수인 경우 answer의 값을 하나 늘리는 식을 넣어준다.
    return answer
