n, m = map(int, input().split())

result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_tmp = min(arr)
    result = max(result, min_tmp)

print(result)
