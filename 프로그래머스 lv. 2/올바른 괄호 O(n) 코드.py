def solution(s):
    answer = True
    arr = list()
    for i in range(0, len(s)):
        if(s[i] == '('):
            arr.append('exit')
        elif(s[i] == ')'):
            if(len(arr) == 0):
                arr.append('none')
            else:
                arr.pop()

    if(len(arr) > 0):
        answer = False

    return answer
