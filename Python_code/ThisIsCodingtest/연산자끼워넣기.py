n = int(input())

min_val = 1e9
max_val = -1e9
arr = list(map(int, input().split()))
# 연산자 갯수
add, sub, mul, div = map(int, input().split())

def dfs(pos, cur_res):
    global min_val, max_val, add, sub, mul, div
    # 모든 연산자 다 사용했을 때, 최솟 값 최댓 값 업데이트
    if pos == n:
        min_val = min(min_val, cur_res)
        max_val = max(max_val, cur_res)
    else :
        if add > 0:
            add -= 1
            dfs(pos + 1, cur_res + arr[pos])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(pos + 1, cur_res - arr[pos])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(pos + 1, cur_res * arr[pos])
            mul += 1
        if div > 0:
            div -= 1
            dfs(pos + 1, int(cur_res / arr[pos]))
            div += 1

dfs(1, arr[0])

print(max_val)
print(min_val)