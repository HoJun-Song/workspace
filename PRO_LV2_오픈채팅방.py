#2022-05-21 2차시도
def solution(record):
    answer = []
    tmp = []
    for sentence in record:
        act = sentence.split(" ")
        if act[0] == 'Enter':
            tmp.append([act[1], act[2], "님이 들어왔습니다."])
            for i in tmp:
                if i[0] == act[1]:
                    i[1] = act[2]
        elif act[0] == 'Leave':
            for i in tmp:
                if i[0] == act[1]:
                    tmp.append([act[1], i[1], "님이 나갔습니다."])
                    break
        else:
            for i in tmp:
                if i[0] == act[1]:
                    i[1] = act[2]
    for i in tmp:
        answer.append(i[1] + i[2])
    return answer
