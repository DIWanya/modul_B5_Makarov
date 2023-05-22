def manual():
    print('Правила игры "Крестики- нолики"')
    print('Вводите по очереди два числа от 0 до 2')
    print('Первое число- номер строки')
    print('Второе число- номер столбца')
board = [['', '', ''] for i in range(3)]
def show_board():
    print('УДАЧИ!!!')
    print(f'  0 1 2')
    for i in range(3):
        row = ' '.join(board[i])
        print(f'{i} {row}')
def make_input():
    while True:
        num = input('Введите числа: ').split()
        if len(num) != 2:
            print('Введите 2 числа!')
            continue
        x, y = num
        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите цифры')
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Введите цифры от 0 до 2')
            continue
        if board[x][y] != '':
            print('Эта клетка уже занята')
            continue
        return x, y
def winner():
    win_komb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for komb in win_komb:
        symbol = []
        for a in komb:
            symbol.append(board[a[0]][a[1]])
        if symbol == ['x', 'x', 'x']:
            print('Выиграл х')
            return True
        if symbol == ['0', '0', '0']:
            print('Выиграл 0')
            return True
    return False
manual()
motion = 0
while True:
    motion += 1
    show_board()
    if motion % 2 == 1:
        print('Поставте крестик')
    else:
        print('Поставте нолик')
    x, y = make_input()
    if motion % 2 == 1:
        board[x][y] = 'x'
    else:
        board[x][y] = '0'
    if winner():
        break
    if motion == 9:
        print('Ничья')
        break
