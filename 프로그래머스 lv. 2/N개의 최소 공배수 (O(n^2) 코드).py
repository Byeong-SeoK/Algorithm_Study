def solution(arr):
    answer = 0
    number = max(arr)
    
    while True:
        find = True
        for i in range(0, len(arr)):
            if(number % arr[i] != 0):
                find = False
                break
            else:
                find = True
                
        if(find):
            break
            
        number = number+1
        
    answer = number
    return answer
