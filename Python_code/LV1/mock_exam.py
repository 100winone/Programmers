def solution(answers):
    answer = []
    correct_arr = []
    picked_way = [[1, 2, 3, 4, 5]
                , [2, 1, 2, 3, 2, 4, 2, 5]
                , [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(len(picked_way)):
        cnt = 0
        for j in range(len(answers)):
            k = j % len(picked_way[i])
            if answers[j] == picked_way[i][k]:
                cnt += 1
        correct_arr.append(cnt)
    max_val = max(correct_arr)
    for i in range(len(correct_arr)):
        if correct_arr[i] == max_val:
            answer.append(i + 1)
    return answer