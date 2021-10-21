def get_distance(present, target):
    coordinate = {1: (0, 0), 2: (0, 1), 3: (0, 2)
                , 4: (1, 0), 5: (1, 1), 6: (1, 2)
                , 7: (2, 0), 8: (2, 1), 9: (2, 2)
                , 10: (3, 0), 0: (3, 1), 12: (3, 2)}
    pre_x, pre_y = coordinate[present]
    tar_x, tar_y = coordinate[target]

    return abs(pre_x - tar_x) + abs(pre_y - tar_y)

def solution(numbers, hand):
    answer = ''
    l_list = [1, 4, 7]
    r_list = [3, 6, 9]
    l_press = 10
    r_press = 12
    for target in numbers:
        if target in l_list:
            answer += 'L'
            l_press = target
        elif target in r_list:
            answer += 'R'
            r_press = target
        else:
            l_distance = get_distance(l_press, target)
            r_distance = get_distance(r_press, target)
            if (l_distance < r_distance):
                answer += 'L'
                l_press = target
            elif (l_distance > r_distance):
                answer += 'R'
                r_press = target
            else:
                if hand == "right":
                    answer += 'R'
                    r_press = target
                else:
                    answer += 'L'
                    l_press = target
    return answer

# 해설
# https://100winone.tistory.com/80