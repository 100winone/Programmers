n = int(input())
data = list(map(int, input().split()))
ans = 0

data.sort()

cnt = 0
for i in data:
    cnt += 1
    if i <= cnt:
        ans += 1
        cnt = 0
print(ans)


