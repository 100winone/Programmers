def solution(s):
    answer = ''
    num = {"zero" : '0', "one" : '1', "two" : '2', "three" : '3'
         , "four" : '4', "five" : '5', "six" : '6', "seven" : '7'
         , "eight" : '8', "nine" : '9' }
    tmp_words = ""
    for i in s:
        if i.isdigit():
            answer += i
            continue
        tmp_words += i
        if tmp_words in num.keys():      # dictionary key 안에 단어가 존재한다면
            answer += num.get(tmp_words)
            # num[tmp_words]
            tmp_words = ""

    return int(answer) # int형으로 변환

# 해설
# https://100winone.tistory.com/80