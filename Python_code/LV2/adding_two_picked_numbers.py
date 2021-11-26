import itertools


def solution(numbers):
    answer = set()
    cb = list(itertools.combinations(numbers, 2))
    for x, y in cb:
        answer.add(x + y)
    answer = sorted(list(answer))

    return answer