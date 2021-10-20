def solution(lottos, win_nums):
    answer = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]
    ans = 0
    zero_cnt = lottos.count(0)
    for i in win_nums:
        if i in lottos:
            ans += 1
    answer[0] = rank[ans + zero_cnt]
    answer[1] = rank[ans]
    return answer
# 해설 https://100winone.tistory.com/79