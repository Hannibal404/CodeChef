t = int(input())
for _ in range(t):
    k = int(input())
    board = [['X' for i in range(8)] for j in range(8)]
    board[0][0] = 'O'
    k -= 1
    if k > 0:
        for i in range(8):
            for j in range(8):
                if i == 0 and j == 0:
                    continue
                if k > 0:
                    board[i][j] = '.'
                    k -= 1
                else:
                    break
            if k < 1:
                break
    for i in board:
        print("".join(i))
