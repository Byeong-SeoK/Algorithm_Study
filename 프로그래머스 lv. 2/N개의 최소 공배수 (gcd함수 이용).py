def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = n * answer / gcd(n, answer)
        
    return answer
