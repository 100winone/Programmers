# 뒤집기 (SILVER 5)
# https://www.acmicpc.net/problem/1439
# 그리디
# 20220417

s = input()
zero_turn = 0
one_turn = 0
prev_num = s[0]

# 1 뒤집을 경우
if prev_num == '1':
    one_turn += 1
else:
    zero_turn += 1

for i in range(1, len(s)):
    if s[i] == '1' and s[i] != prev_num:
        one_turn += 1
    elif s[i] == '0' and s[i] != prev_num:
        zero_turn += 1
    prev_num = s[i]

print(min(zero_turn, one_turn))