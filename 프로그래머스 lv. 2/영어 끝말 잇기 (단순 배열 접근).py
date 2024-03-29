def solution(n, words):
    answer = []

    used = {}
    # 이미 사용된 단어를 받는 dictionary이다.

    count = 1
    # 몇번째 사람이 언급할 차례인지 받는 변수이다.

    end_if = False
    # 끝에 도달했는지 확인하는 boolean 변수이다.

    for i in range(0, len(words)):
        if (words[i] in used):
            # 앞에서 언급한 단어를 또 언급한 경우
            # 해당 사람은 탈락하게 된다.

            answer.append(count)
            answer.append((i // n) + 1)
            # 차례를 구하기 위해서는 해당 단어의 index를
            # 사람 수(n)로 나누어서 +1을 하면 된다.
            # TC1 경우 tank가 8번째 index를 가지고 있는데
            # 이 index를 3으로 나누면 2이고 거기에 +1을 하여
            # 해당 단어가 몇번째 등장한 것인지 구할 수 있다.

            end_if = False
            # 끝까지 도달하지 못하였으므로 False로 선언

            break

        else:
            if (len(used) == 0):
                # 사전에 아무것도 없는 상황에서는 바로 집어넣도록 한다.

                used[words[i]] = 1
                # 사전에 해당 단어를 넣는다.

                if(count == n):
                    # n번째 사람까지 한번씩 다 단어를 말한 경우
                    count = 1
                else:
                    count = count+1

                continue
                # continue를 해주는 이유는 아래의 if문을 건너뛰기 위함이다.

            else:
                if (words[i - 1][len(words[i - 1]) - 1] == words[i][0]):
                    # 이전 사람이 언급한 마지막 단어와 지금 사람이 언급한
                    # 첫번째 단어가 같으면 올바르게 넘어가도록 한다.

                    used[words[i]] = 1
                    # 사전에 해당 단어를 넣는다.

                    if(count == n):
                        #n번째 사람까지 한번씩 다 단어를 말한 경우
                        count = 1
                    else:
                        count = count + 1
                        # 다음 사람에게 차례를 넘긴다.

                    end_if = True
                    continue
                    #continue를 해주는 이유는 아래의 if문을 건너뛰기 위함이다.

                else:
                    # 앞의 사람이 말한 단어 끝자리와
                    # 뒤의 사람이 말한 단어 첫자리가 다른 경우

                    answer.append(count)
                    answer.append((i // n) + 1)

                    end_if = False
                    break

            if (i == len(words) - 1):
                end_if = True

    if (end_if):
        answer = [0, 0]

    return answer
