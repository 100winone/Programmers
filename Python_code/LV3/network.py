checked = [0 for _ in range(201)]


def bfs(n, computers ,x):
    # q = []
    # q.append(x) 아래 하나로 선언
    q = [x]
    while len(q) != 0:
        cur = q.pop(0)
        checked[cur] = 1
        for i in range(0, n):
            if checked[i] == 0:
                if computers[cur][i]:
                    checked[i] = 1
                    q.append(i)


def solution(n, computers):
    answer = 0
    for i in range(0, len(computers)):
        if checked[i] == 0:
            bfs(n, computers, i)
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))