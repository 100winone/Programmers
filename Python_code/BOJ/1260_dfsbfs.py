import sys
from collections import deque
read = sys.stdin.readline

def dfs(v):
    checked[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if checked[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    checked[v] = 1
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for i in range(1, n + 1):
            if graph[cur][i] == 1 and checked[i] == 0:
                queue.append(i)
                checked[i] = 1

n, m, v = map(int, read().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
checked = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, read().split())
    graph[x][y] = graph[y][x] = 1

dfs(v)
checked = [0] * (n + 1)
print()
bfs(v)
