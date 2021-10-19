import re

def dot_deleted(ans):
    if ans[0] == '.':
        ans = ans[1:]
    elif ans[-1] == '.':
        ans = ans[:-1]
    return ans

def solution(new_id):
    answer = ""

    # 1단계 소문자로 변경
    tmp = new_id.lower()

    # 2단계 허용되는 문자만 사용
    for i in tmp:
        if i.isalpha() or i.isdigit() or (i == '-') or (i == '-') or (i == '_') or (i == '.'):
            answer += i

    # 3단계 연속된 '.' 하나로 만들기
    answer = re.sub('[.]+', '.', answer) # 정규식 연속된거 +로 체크

    # 4단계 아이디 처음에 위치한 '.'제거
    answer = dot_deleted(answer)
    # print(answer)
    # if answer[0] == '.':
    #     answer = answer[1:]
    # elif answer[-1] == '.':
    #     answer = answer[:-1]

    # 5단계 빈문자열이면 'a'
    if len(answer) == 0:
        answer = 'a'

    # 6단계 길이 16자 이상이면 처음 15자까지만
    if len(answer) > 15:
        answer = answer[:15]
    answer = dot_deleted(answer)

    # 7단계 아이디가 2자 이하라면 마지막문자를 길이가 3이될 때 까지 붙임
    while len(answer) <= 2:
        answer = answer + answer[-1]
    return answer