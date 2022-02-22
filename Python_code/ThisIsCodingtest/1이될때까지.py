n, k = map(int, input().split())
val_n = n
cnt = 0

while val_n != 1:
    cnt += 1
    if val_n % k == 0:
        val_n /= k
    else:
        val_n -= 1

print(cnt)
