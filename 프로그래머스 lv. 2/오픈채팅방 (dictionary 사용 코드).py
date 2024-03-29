def solution(record):
    answer = []
        
    chat_order = [] #톡방 출입 순서를 저장할 배열
    chat_id = [] #톡방에 있는 사람들의 id값을 저장하는 배열
    chat_name = [] #톡방에 있는 사람들의 닉네임
    
    for i in range(0, len(record)):
        record[i] = record[i].split(' ')
        
        if(record[i][0] == 'Enter'):
            chat_order.append(record[i][0])
            chat_id.append(record[i][1])
            chat_name.append(record[i][2])
        elif(record[i][0] == 'Leave'):
            chat_order.append(record[i][0])
            chat_id.append(record[i][1])
            chat_name.append('None')
        else:
            chat_order.append(record[i][0])
            chat_id.append(record[i][1])
            chat_name.append(record[i][2])
    
    #print(chat_order)
    #print(chat_id)
    #print(chat_name)
    
    chat_room = dict() #톡방에 남아있는 사람의 아이디와 닉네임을 갖는 사전
                       #여기서 아이디를 key값으로 닉네임이 value값이 된다.
    for j in range(0, len(chat_order)):
        if(chat_order[j] == 'Enter'):
            chat_room[chat_id[j]] = chat_name[j]
            #닉네임 변경후 나간 다음 재입장하더라도 사전의 key값의 value만 바꾸면 된다.
        elif(chat_order[j] == 'Leave'):
            if(chat_room.get(chat_id[j]) == 'None'):
                continue
            else:
                #del(chat_room[chat_id[j]])
                #del을 사용하면 밑의 for문을 통해서 answer를 만들때
                #존재하지 않는 key값에 접근하는 상황이 생기므로 임시로
                #user의 닉네임을 empty로 바꾸고 밑에서 empty일때는 무시하도록 한다.
                chat_room[chat_id[j]] == 'empty'
        else:
            chat_room[chat_id[j]] = chat_name[j]
    #print(chat_room)
    
    for m in range(0, len(chat_order)):
        name = ''
        if(chat_order[m] == 'Enter'):
            name = chat_room[chat_id[m]]
            name = name + '님이 들어왔습니다.'
            answer.append(name)
        elif(chat_order[m] == 'Leave'):
            if(chat_room.get(chat_id[m]) == 'empty'):
                continue
            else:
                name = chat_room[chat_id[m]]
                name = name + '님이 나갔습니다.'
                answer.append(name)
        else:
            continue
        
    #print(answer)
    return answer
