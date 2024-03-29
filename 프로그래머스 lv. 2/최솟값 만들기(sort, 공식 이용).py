def solution(A,B):
    answer = 0
    
    """
    배열 A, B를 각각 sort 한 다음
    A는 index가 큰 순서대로 접근하고
    B는 index가 작은 순서대로 접근하여
    각각을 곱하여 모두 더한 값이 가장 최소가 된다.
    """
    
    A.sort()
    B.sort()
    
    length = len(A)
    
    for i in range(0, length):
        answer = answer + (A[len(A)-1-i] * B[i])
    
    return answer
