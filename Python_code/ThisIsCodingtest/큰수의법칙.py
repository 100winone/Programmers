n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
arr.sort()

first = arr[-1]
second = arr[-2]
for i in range(1, m + 1):
    if i % k == 0:
        sum += second
        continue
    sum += first

print(sum)




