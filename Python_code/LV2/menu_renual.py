from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for menu_cnt in course:
        tmp = []
        for order in orders:
            comb = combinations(sorted(order), menu_cnt)
            tmp += comb
        counter = Counter(tmp)

        if len(counter) > 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)