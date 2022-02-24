def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    return False

n, m = map(int, input().split())

# 2차원리스트에 값 넣기
graph = []
for i in range(n):
    graph.append(list(map(int, (input())))) #

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)