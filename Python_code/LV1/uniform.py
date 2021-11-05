def solution(n, lost, reserve):
    answer = 0
    checked = [True for _ in range(5)]

    for i in lost:
        checked[i - 1] = False
    
    for i in range(1, n - 1):
        # if checked[i] == False:



    # print(checked)
    return answer

print(solution(5, [2, 4], [1, 3, 5]))