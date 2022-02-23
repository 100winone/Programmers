input_data = input()
col = int(ord(input_data[0])) - int(ord('a')) + 1
row = int(input_data[1])
answer = 0
steps = [(-1, -2), (1, -2), (1, 2), (-1, 2), (-2, 1), (-2, -1), (2, -1), (2, 1)]

for steps_val in steps:
    row_tmp = row + steps_val[0]
    col_tmp = col + steps_val[1]
    if row_tmp < 1 or row_tmp > 8 or col_tmp < 1 or col_tmp > 8:
        continue
    answer += 1

print(answer)