def solution(prices):
    answer = []
    
    for i in range(0, len(prices)):
        maintain = 0
        for j in range(i, len(prices)):
            if(i == j):
                continue
            else:
                if(prices[j] >= prices[i]):
                    maintain = maintain+1
                else:
                    maintain = maintain+1
                    break
        answer.append(maintain)
                    
    return answer
