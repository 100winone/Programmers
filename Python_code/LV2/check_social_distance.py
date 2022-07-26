from collections import deque

def bfs(place):
    applicant = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                applicant.append((i, j))

    for x, y in applicant:
        q = deque([(x, y)])
        checked = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        checked[x][y] = 1

        while q:
            cur_x, cur_y = q.popleft()
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and checked[nx][ny] == 0:
                    if place[nx][ny] == 'O':
                        q.append((nx, ny))
                        distance[nx][ny] = distance[cur_x][cur_y] + 1

                        checked[nx][ny] = 1
                    if place[nx][ny] == 'P':
                        if distance[cur_x][cur_y] <= 1:
                            return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer