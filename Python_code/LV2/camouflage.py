def solution(clothes):
    dic_closet = {}
    answer = 1

    for cloth in clothes:
        if cloth[1] in dic_closet.keys():
            dic_closet[cloth[1]].append(cloth[0])
        else :
            dic_closet[cloth[1]] = [cloth[0]]
            # dic_closet[cloth[1]] = cloth[0]


    for value in dic_closet.values():
        answer *= len(value) + 1
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))