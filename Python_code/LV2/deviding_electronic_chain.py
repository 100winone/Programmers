answer = 0


def bfs(wires, checked, num, cnt):
    global answer
    q = [num]
    while len(q) != 0:
        cur = q.pop(0)
        for i in range(0, len(wires)):
            if wires[i][0] == cur:
                if checked[wires[i][1]] == 0:
                    checked[wires[i][1]] = 1
                    q.append(wires[i][1])
                    cnt += 1
            elif wires[i][1] == cur:
                if checked[wires[i][0]] == 0:
                    checked[wires[i][0]] = 1
                    q.append(wires[i][0])
                    cnt += 1
    tmp_len = len(wires) + 1
    tmp = abs(cnt - (tmp_len - cnt))
    answer = min(answer, tmp)

    return answer


def solution(n, wires):
    global answer
    answer = 1000
    for i in range(0, n - 1):
        checked = [0 for _ in range(102)]
        checked[wires[i][0]] = 1
        checked[wires[i][1]] = 1
        bfs(wires, checked, wires[i][0], 1)

    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))

# https://100winone.tistory.com/82