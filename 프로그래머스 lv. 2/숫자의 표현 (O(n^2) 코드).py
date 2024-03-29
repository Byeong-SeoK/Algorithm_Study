def solution(n):
    answer = 0
    
    li = [0] * n #1부터 n까지의 수를 저장할 배열
    for i in range(0, n):
        li[i] = i+1
    
    sum = 0
    for j in range(0, n): #연속적인 수의 합이 n이 되어야 하므로 시작점을 오름차순으로 늘려나간다
        for k in range(j, n): #시작점은 고정을 시켜놓은 상태에서 연속적인 수들의 합을 구한다.
            sum = sum + li[k]
            
            if(sum == n): #연속적인 수들의 합이 n과 같으면 시작점을 한칸 뒤로 옮긴다.
                answer = answer + 1
                sum = 0
                break
            elif(sum > n): #연속적인 수들의 합이 n보다 크면 시작점을 한칸 뒤로 옮긴다.
                sum = 0
                break
            else:
                continue
            
    return answer
