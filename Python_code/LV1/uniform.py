def solution(n, lost, reserve):
    answer = n - len(lost)
    lost_person = ["False" for _ in range(n)]
    extra_uniform = ["False" for _ in range(n)]

    for i in lost:
        lost_person[i - 1] = "True"          # 잃어버린 학생 "True"
    for i in reserve:
        extra_uniform[i - 1] = "True"        # 여분의 유니폼 학생 "True"
        if lost_person[i - 1] == "True":     # 여벌 체육복 가져온 학생이 도난 당한 경우
            extra_uniform[i - 1] = "False"
            lost_person[i - 1] = "False"
            answer += 1

    # 첫 번째 인덱스 별도 처리
    if lost_person[0] == "True":
        if extra_uniform[1] == "True":
            answer += 1
            lost_person[0] = "False"
            extra_uniform[1] = "False"

    for i in range(1, n - 1):
        if lost_person[i] == "True":
            if extra_uniform[i - 1] == "True":
                answer += 1
                lost_person[i] = "False"
                extra_uniform[i - 1] = "False"
            elif extra_uniform[i + 1] == "True":
                answer += 1
                lost_person[i] = "False"
                extra_uniform[i + 1] = "False"
    # 마지막 인덱스 별도 처리
    if lost_person[n - 1] == "True":
        if extra_uniform[n - 2] == "True":
            answer += 1

    return answer