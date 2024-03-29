def solution(s):
    answer = []

    zero_count = 0
    # 첫번째 변환에서 지워진 0의 개수를 받는 변수이다.

    loop = 0
    # 몇 회차의 변환을 거쳐야하는지 받는 변수이다.

    while (s != '1'):
        transition = ""
        # 첫번째 변환을 받는 string 변수이다.

        for i in range(0, len(s)):
            if (s[i] == '0'):
                zero_count = zero_count + 1
                # 지워진 0의 개수를 하나 늘린다.
            else:
                transition = transition + s[i]

        c = len(transition)
        # 두번째 변환을 하기 위해 transition의 길이를 받는다.
        transition = format(c, 'b')

        s = transition
        #최종적으로 변환된 값을 s에 넣도록 한다.

        loop = loop + 1
        # 두번째 변환까지 끝났으므로 loop를 1 늘린다.

    answer.append(loop)
    answer.append(zero_count)

    return answer
