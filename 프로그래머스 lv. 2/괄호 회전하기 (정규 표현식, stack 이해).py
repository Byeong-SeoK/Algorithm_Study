def solution(s):
    answer = 0

    word = []
    for i in range(0, len(s)):
        #string은 내부 수정이 안되므로 배열로 변환한다.
        word.append(s[i])

    Max = len(word) #회전 횟수의 최댓값
    x = 0 #회전 횟수
    while (x < Max):
        if(word[0] == ')' or word[0] == '}' or word[0] == ']'):
            #시작이 ), }, ]이면 항상 올바른 짝을 지을 수 없다.
            word.append(word.pop(0))

        else:
            stack = [] #올바른 짝을 이루는지 판단하는 스택
            """
            아래와 같이 스택의 가장 오른쪽의 값과 배열의 가장 왼쪽 값을
            비교하는 이유는 정규 표현식 문제가 있어서 그렇다.
            예를 들어 TC가 "([{)}]"인 경우 각 괄호 모두 올바른 짝을
            이룰 수 있지만 () 같은 괄호 안에 항상 올바르게 짝을 이룬
            괄호가 있어야한다는 정규 표현식을 만족하지 못하므로 결국
            해당 TC는 항상 올바른 짝을 이루지 못하는 것이 된다.
            그러므로 정규 표현식을 만족하려면 () 같은 괄호 안에 항상 []와
            같은 올바른 짝이 들어있어야 한다. 그래서 만약 stack에 ([ 이 들어있고
            정규 표현식을 만족하는 TC라면 word의 가장 왼쪽 첫번째는 ]이 되고
            두번째는 )이 나와야한다. 따라서 stack의 가장 오른쪽과 word의 가장
            왼쪽을 서로 비교해보면 된다.
            """

            for j in range(0, Max):
                #a[-1]: 배열 a의 오른쪽에서 첫번째 값.
                #파이썬에서 -는 오른쪽, +는 왼쪽
                if(len(stack) > 0):
                    if(stack[-1] == '(' and word[j] == ')'):
                        #stack에서 가장 오른쪽에 있는 것과 비교를 해서
                        #같으면 pop을 하도록 한다.
                        stack.pop()
                    elif(stack[-1] == '{' and word[j] == '}'):
                        stack.pop()
                    elif(stack[-1] == '[' and word[j] == ']'):
                        stack.pop()
                    else:
                        stack.append(word[j])
                else:
                    #( 다음에 ( 이 온 경우에 해당한다.
                    #이때도 그냥 ( 를 stack에 추가한다.
                    #그냥 continue로 넘겨버리면 ()( 를 ()로 간주해버리게 된다.
                    stack.append(word[j])

            if(len(stack) == 0):
                #모든 괄호가 올바르게 짝지어졌으면 stack의 길이는 0이 된다.
                answer = answer+1

            #가장 앞에 있는 괄호를 뒤로 보내 회전시킨다.
            word.append(word.pop(0))

        x = x+1

    return answer
