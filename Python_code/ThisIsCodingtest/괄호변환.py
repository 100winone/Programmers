# 균형잡힌 문자열 위치임과 동시에 올바른 문자열인지 확인
def parse(str):
    correct = True
    left = 0
    right = 0
    myStack = []
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            myStack.append('(')
        else:
            right += 1
            if len(myStack) == 0:
                correct = False
            else:
                myStack.pop()
        if left == right:
            return i + 1, correct

    return 0


def solution(p):
    if len(p) == 0:
        return p

    # 위치 찾는 함수
    index, correct = parse(p)
    u = p[:index]
    v = p[index:]

    if correct:
        return u + solution(v)

    answer = '(' + solution(v) + ')'

    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('

    return answer