n = input()
len_n = len(n)

left = n[:(len_n // 2)]
right = n[(len_n // 2):]
sum = 0
for i in left:
    sum += int(i)

for i in right:
    sum -= int(i)

print("LUCKY" if sum == 0 else "READY")

    # print("LUCKY")
# else: print("READY")