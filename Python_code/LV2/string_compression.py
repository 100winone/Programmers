def solution(s):
    answer = 1001
    max_len = len(s) // 2

    if len(s) == 1: return 1

    for i in range(1, max_len + 1):  # 자를 문자열의 갯수
        tmp_str = ""
        prev_str = s[:i]  # 비교할 문자열 저장
        cnt = 1
        for j in range(i, len(s), i):
            if s[j:j + i] == prev_str:
                cnt += 1
            else:
                tmp_str += str(cnt) + prev_str if cnt >= 2 else prev_str
                prev_str = s[j:j + i]
                cnt = 1
        tmp_str += str(cnt) + prev_str if cnt >= 2 else prev_str
        answer = min(answer, len(tmp_str))
    return answer