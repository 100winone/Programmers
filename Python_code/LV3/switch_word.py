answer = 987654321
checked = [False for _ in range(51)]


def diff(word_a, word_b):
    len_word = len(word_a)
    cnt = 0
    for i in range(len_word):
        if word_a[i] != word_b[i]:
            cnt += 1
    return True if cnt == 1 else False


def dfs(begin, target, words, cnt):
    global answer
    for i in range(len(words)):
        if begin == target:
            answer = min(answer, cnt)
            return
        if diff(begin, words[i]) and not checked[i]:
            checked[i] = True
            dfs(words[i], target, words, cnt + 1)
            checked[i] = False
    # return


def solution(begin, target, words):
    if target not in words:
        return 0
    dfs(begin, target, words, 0)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# answer = 101
# check = [0 for _ in range(51)]
#
#
# def diff(a_word, b_word):
#     dif_cnt = 0
#     for i in range(0, len(a_word)):
#         if a_word[i] != b_word[i]:
#             dif_cnt += 1
#
#     return 1 if dif_cnt == 1 else 0
#
#
# def dfs(begin, target, words, cnt):
#     global answer
#
#     for i in range(0, len(words)):
#         if diff(begin, words[i]) == 1:
#             if target == words[i]:
#                 if answer > cnt + 1:
#                     answer = cnt + 1
#                     return
#             if check[i] == 0:
#                 check[i] = 1
#                 dfs(words[i], target, words, cnt + 1)
#                 check[i] = 0
#
#
# def solution(begin, target, words):
#     if target not in words:
#         return 0
#
#     dfs(begin, target, words, 0)
#
#     return answer
#
#
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
