from random import random, choice, randint


VAR_L = 0.05
SIZE = 4


def reprmat(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end='\t')
        print()


def create_board(size=8):
    s = [[0 for i in range(size)] for j in range(size)]
    for i in (0, 1):
        i = randint(0, size - 1)
        j = randint(0, size - 1)
        s[i][j] = 2
    return s


def matrix_copy(matrix, tr=0):
    res = []
    for i in range(len(matrix)):
        res.append([])
        for j in range(len(matrix[i])):
            if tr:
                res[i].append(matrix[j][i])
            else:
                res[i].append(matrix[i][j])
    return res


def move(board, direct='a'):
    tr = 0
    if direct in 'ws':
        tr = 1
    s = matrix_copy(board, tr)
    dr = (0, len(s), 1)
    if direct not in 'aw':
        dr = (len(s) - 1, -1, -1)
    for i in range(len(board)):
        cur = dr[0]
        for j in range(*dr):
            if s[i][j] == 0:
                continue
            if s[i][cur] == 0:
                s[i][cur], s[i][j] = s[i][j], s[i][cur]
                continue
            if s[i][cur] == s[i][j] and cur != j:
                s[i][cur] *= 2
                s[i][j] = 0
                cur += dr[2]
            elif s[i][cur] != s[i][j]:
                cur += dr[2]
                s[i][cur], s[i][j] = s[i][j], s[i][cur]
    return matrix_copy(s, tr)


def add_rd(board, rd=0.05):
    s = matrix_copy(board)
    cs = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                cs.append((i, j))
    if not cs:
        if s == move(s) and s == move(s, 'd') and \
           s == move(s, 'w') and s == move(s, 's'):
            return 1
        else:
            return 0
    cs = choice(cs)
    if random() < rd:
        rdint = 4
    else:
        rdint = 2
    s[cs[0]][cs[1]] = rdint
    return s


def turn(s, direct='a', rd=0.05):
    if type(s) == int:
        return s
    return add_rd(move(s, direct), rd)


if __name__ == '__main__':
    board = create_board(SIZE)
    reprmat(board)
    while True:
        inp = input('Введите направление: ')
        if inp not in 'wsad' or inp == '':
            continue
        ccc = turn(board, inp, VAR_L)
        if ccc == 1:
            print("Вы проиграли")
            break
        if ccc == 0:
            continue
        board = ccc
        reprmat(board)
