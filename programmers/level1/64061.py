def solution(board, moves):
    basket = []
    answer = 0
    N = len(board)

    for row_pos in moves:
        col_pos = 0
        row_pos -= 1
        while True:
            if col_pos >= N:
                break
            if board[col_pos][row_pos] != 0:
                if len(basket) > 0 and basket[-1] == board[col_pos][row_pos]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[col_pos][row_pos])
                board[col_pos][row_pos] = 0
                break
            else:
                col_pos += 1

    return answer