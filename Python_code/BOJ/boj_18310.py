# 국영수 (SILVER 3)
# https://www.acmicpc.net/problem/18310
# 정렬
# 20220420

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[(n - 1) // 2])

# 시간초과 풀이
# n = int(input())
# answer = 987654321
# coordinate = 200001
# arr = list(map(int, input().split()))
# arr.sort()
# min_val = min(arr)
# max_val = max(arr)
#
# for antenna in range(min_val, max_val + 1):
#     tmp_val = 0
#     for i in arr:
#         tmp_val += abs(i - antenna)
#     if answer > tmp_val:
#         coordinate = antenna
#         answer = tmp_val
#     # coordinate = antenna if answer < tmp_val else coordinate
#     # answer = min(answer, tmp_val)
#
# print(coordinate)