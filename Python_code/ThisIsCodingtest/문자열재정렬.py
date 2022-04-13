s = input()
ans = 0
tmp_str = ""
for i in s:
    if 1 <= ord(i) - 48 <= 9:
        ans += int(i)
    else: tmp_str += i

sum_str = ''.join(sorted(tmp_str))
print(sum_str + str(ans))
