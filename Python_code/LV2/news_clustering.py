from collections import Counter


def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    arr1 = [str1[i:i + 2] for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]  # 한번에 해결
    arr2 = [str2[i:i + 2] for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]  # 한번에 해결
    if len(arr1) == 0 and len(arr2) == 0:
        return 65536
    c1 = Counter(arr1)
    c2 = Counter(arr2)

    sum_set = sum((c1 | c2).values())
    inter_set = sum((c1 & c2).values())
    answer = (inter_set / sum_set) * 65536
    return int(answer)