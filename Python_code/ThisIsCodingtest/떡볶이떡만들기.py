n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

start = 0
end = max(arr)

while start <= end:
    tot = 0
    mid = (end + start) // 2

    for x in arr:
        if x > mid:
            tot += x - mid

    if tot >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
