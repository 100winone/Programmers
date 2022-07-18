# answer = 0
# def solution(numbers, target):
#     def dfs(cnt, sum):
#         global answer
#         if cnt == len(numbers):
#             if sum == target:
#                 answer += 1
#             return
#
#         dfs(cnt + 1, sum - numbers[cnt])
#         dfs(cnt + 1, sum + numbers[cnt])
#
#     dfs(0, 0)
#     return answer

answer = 0

def dfs(idx, numbers, target, cur_sum):
    global answer
    if idx == len(numbers):
        if cur_sum == target:
            answer += 1
        return
    dfs(idx + 1, numbers, target, cur_sum + numbers[idx])
    dfs(idx + 1, numbers, target, cur_sum - numbers[idx])


def solution(numbers, target):
    dfs(0, numbers, target, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
# 종료조건과 재귀로 호출할 형태 구성
