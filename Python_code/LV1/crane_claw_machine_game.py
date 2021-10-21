def solution(board, moves):
    answer = 0
    basket = []
    row_size = len(board)

    for i in moves:
        index = i - 1
        for j in range(row_size):
            if board[j][index] != 0:
                if len(basket) == 0:                  # 바구니가 비어있다면
                    basket.append(board[j][index])    # 바구니에 담아주고
                else:
                    if basket[-1] == board[j][index]: # 바구니의 마지막 값과 뽑은 인형의 값이 같을 때
                        answer += 2                   # 깨진 인형의 수를 더해줌
                        basket.pop()                  # 바스켓에 있는 마지막 값을 비워줌
                    else:
                        basket.append(board[j][index])  # 바구니에 담아줌
                board[j][index] = 0  # 인형뽑기 값을 0으로 비워줌
                break
    return answer

# 해설
# https://100winone.tistory.com/82