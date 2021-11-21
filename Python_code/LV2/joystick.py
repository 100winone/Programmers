def solution(name):
    answer = 0
    # 문자를 배열 숫자로 변경 -> ascii로 변경하여 최소 순서
    arr_name = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0
    while True:
        answer += arr_name[idx]
        arr_name[idx] = 0
        if sum(arr_name) == 0:
            break

        left, right = 1, 1
        while arr_name[idx - left] == 0:
            left += 1
        while arr_name[idx + right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right
    return answer