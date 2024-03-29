from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보
data = [] # 바이러스 정보

for i in range(n):
    graph.append(list(map(int, input().split()))) # 리스트로 주기 위해 list로 감싸줌
    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, 위치 X, 위치 Y 삽입
            data.append((graph[i][j], 0, i, j))
# 정렬 이후에 큐로 옮기기 ( 낮은 번호의 바이러스가 먼저 증식하기 때문 )
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split()) # map으로 하면 하나씩

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 진행
while q:
    virus, s, x, y = q.popleft()
    # s초가 지나거나, 큐가 빌 때 까지 반복
    if s == target_s:
        break

    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx < n and 0 <= ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])