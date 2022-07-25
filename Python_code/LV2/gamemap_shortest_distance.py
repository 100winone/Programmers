from collections import deque

checked = [[0] * 101 for _ in range(101)]

def bfs(x, y, maps):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    q = deque([(x, y)])
    checked[x][y] = 1
    distance = {(x, y): 0}
    n, m = len(maps), len(maps[0])
    while q:
        cur_x, cur_y = q.popleft()
        # return -1
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if checked[nx][ny] == 0 and maps[nx][ny] == 1:
                    if (nx, ny) == (n - 1, m - 1):
                        return distance[(cur_x, cur_y)] + 2
                    checked[nx][ny] = 1
                    q.append((nx, ny))
                    distance[(nx, ny)] = distance[(cur_x, cur_y)] + 1
    return -1


def solution(maps):
    n, m = len(maps), len(maps[0])

    return bfs(0, 0, maps)
