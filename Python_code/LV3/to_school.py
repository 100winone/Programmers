def solution(m, n, puddles):
    arr = [[0] * (m + 1) for i in range(n + 1)]
    answer = 0
    arr[1][1] = 1

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if x == 1 and y == 1:
                continue
            if [y, x] in puddles:
                arr[x][y] = 0
            else:
                arr[x][y] = arr[x][y - 1] + arr[x - 1][y]

    answer = arr[x][y]

    return answer % 1000000007