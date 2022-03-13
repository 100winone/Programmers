# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
# BFS
# 20220313
from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
d = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    queue = deque([start])
    visited[start] = True
    d[start] = 0
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                d[i] = d[cur] + 1
                if d[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print("-1")
    else:
        answer.sort()
        for i in answer:
            print(i)
bfs(x)