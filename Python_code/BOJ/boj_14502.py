# 연구소 (GOLD 5)
# https://www.acmicpc.net/problem/14502
# DFS
# 20220314
n, m = map(int, input().split())
graph = []
tmp = [[0] * m for _ in range(n)]
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 1. 바이러스를 퍼지도록 하는 def dfs하나
# 2. 점수 세는 def 하나
# 3. 울타리를 모든 곳에 세워보는 경우의 수 하나
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx, ny)


def dfs(count):
    global result

    # 조건이 울타리 3개가 다 쳐진 경우,
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)
        cnt_safe = 0
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 0:
                    cnt_safe += 1

        result = max(result, cnt_safe)
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1


dfs(0)
print(result)