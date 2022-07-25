def solution(record):
    answer = []
    dict_id = {}
    record_len = len(record)

    for i in range(record_len):
        tmp = []
        tmp = list(record[i].split(' '))
        if tmp[0] == 'Enter':
            dict_id[tmp[1]] = tmp[2]
        elif tmp[0] == 'Change':
            dict_id[tmp[1]] = tmp[2]

    # print(dict_id)
    for sentence in record:
        tmp = sentence.split()
        if tmp[0] == 'Enter':
            answer.append(dict_id[tmp[1]] + "님이 들어왔습니다.")
        elif tmp[0] == 'Leave':
            answer.append(dict_id[tmp[1]] + "님이 나갔습니다.")

    return answer