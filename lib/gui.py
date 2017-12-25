import tkinter as tk
import env
from tkinter import messagebox as msg


SIZE = 3
CHS = 100


def init_canv(master, size=4, chs=150):
    master.configure(height=size * chs, width=size * chs)
    master.delete('all')
    master.create_rectangle(0, 0, size * chs + 10, size * chs + 10,
                            fill='#707040')
    for i in range(size):
        for j in range(size):
            master.create_rectangle(i * chs + 2, j * chs + 2,
                                    i * chs + chs - 2, j * chs + chs - 2,
                                    tags=('norm', '%dx%dn' % (i, j)),
                                    fill='silver')
            master.create_text((i + 0.5) * chs, (j + 0.5) * chs, text='',
                               font='Droid 12',
                               tags=('tx', '%dx%dt' % (i, j)))
            master.create_rectangle(i * chs, j * chs,
                                    i * chs + chs, j * chs + chs,
                                    tags=('lg', '%dx%dl' % (i, j)))
    master.tag_lower('lg')
    master.tag_raise('normal')


def swi(canv, n=1):
    global board
    for i in range(n):
        ccc = env.turn(board, 'w')
        ccc = env.turn(ccc, 'a')
        ccc = env.turn(ccc, 's')
        ccc = env.turn(ccc, 'd')
        if type(ccc) != int:
            board = ccc
    move(canv)


def main():
    global board
    root = tk.Tk()
    root.title('2048')
    root.geometry('800x600+100+100')

    canv = tk.Canvas(bg='white', height=500, width=500)
    init_canv(canv, SIZE, CHS)
    board = env.create_board(SIZE)
    canv.pack()
    root.bind('<Left>', lambda x: move(canv, 'w'))
    root.bind('<Right>', lambda x: move(canv, 's'))
    root.bind('<Up>', lambda x: move(canv, 'a'))
    root.bind('<Down>', lambda x: move(canv, 'd'))
    root.bind('1', lambda x: swi(canv, 1))
    root.bind('2', lambda x: swi(canv, 5))
    root.bind('3', lambda x: swi(canv, 10))
    root.bind('4', lambda x: swi(canv, 50))
    root.bind('5', lambda x: swi(canv, 100))
    root.bind('6', lambda x: swi(canv, 500))
    root.bind('7', lambda x: swi(canv, 1000))
    root.mainloop()


def move(canv, direct='a', rd=0.05):
    global board
    sss = env.turn(board, direct, rd)
    if sss == 0 or sss == 1:
        if sss == 1:
            msg.showerror('Win!', 'You are loser!')
        return 0
    board = sss
    for i in range(len(board)):
        for j in range(len(board)):
            txt = str(board[i][j])
            if txt == '0':
                txt = ''
            tk.Canvas.itemconfig(canv, '%dx%dt' % (i, j),
                                 text=txt)


if __name__ == '__main__':
    main()
