def solution(array, commands):
    answer = []
    commands_len = len(commands)
    for index in range(commands_len):
        i = commands[index][0]
        j = commands[index][1]
        k = commands[index][2]
        arr = array[i - 1:j]
        arr.sort()
        answer.append(arr[k - 1])
    return answer
