def solution(s):
    answer = []

    list_s = s[2:-2]
    list_s = list_s.split('},{')
    list_s.sort(key=len)
    for i in list_s:
        ii = i.split(',')

        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))

    return answer