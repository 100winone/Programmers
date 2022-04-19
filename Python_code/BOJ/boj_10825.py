# 국영수 (SILVER 4)
# https://www.acmicpc.net/problem/10825
# 정렬 (필수 문제)
# 20220419

n = int(input())
student = []
for i in range(n):
    student.append(input().split())
student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(n):
    print(student[i][0])
