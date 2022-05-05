
game_table = [[' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' ']]

def get_game_table(table):
    i = 0
    for row in table:
        i += 1
        print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} ")
        if i < 3:
            print("---------")

def add_x_to_table(table):
    row = int(input('Player 1 Chose your row:'))
    column = int(input('Player 1 chose your column:'))
    ErrorCode = 0
    if column == 1:
        column = 0
    elif column == 2:
        column = 2
    elif column == 3:
        column = 4
    else:
        ErrorCode = 1
        return ErrorCode
    if 0 < row < 4:
        if table[row-1][column] == ' ':
            table[row - 1][column] = 'X'
            get_game_table(table)
            ErrorCode = 0
            return ErrorCode
        else:
            ErrorCode = 2
            return ErrorCode

    else:
        ErrorCode = 1
        return ErrorCode

def add_o_to_table(table):
    ErrorCode = 0
    row = int(input('Player 2 Chose your row:'))
    column = int(input('Player 2 chose your column:'))
    if column == 1:
        column = 0
    elif column == 2:
        column = 2
    elif column == 3:
        column = 4
    else:
        ErrorCode = 1
        return ErrorCode
    if 0 < row < 4:
        if table[row-1][column] == ' ':
            table[row - 1][column] = 'O'
            get_game_table(table)
            ErrorCode = 0
            return ErrorCode
        else:
            ErrorCode = 2
            return ErrorCode

    else:
        ErrorCode = 1
        return ErrorCode


def who_win(table):
    column_1 = [table[0][0], table[1][0], table[2][0]]
    column_2 = [table[0][2], table[1][2], table[2][2]]
    column_3 = [table[0][4], table[1][4], table[2][4]]
    x_1 = [table[0][0], table[1][2], table[2][4]]
    x_2 = [table[0][4], table[1][2], table[2][0]]
    table_column = [column_1, column_2, column_3]
    table_x_axis = [x_1, x_2]
    for row in table:
        if row.count('X') == 3:
            return f"Player 1 win"
        elif row.count('O') == 3:
            return f"Player 2 win"
    for column in table_column:
        if column.count('X') == 3:
            return f"Player 1 win"
        elif column.count('O') == 3:
            return f"Player 2 win"
    for x_axis in table_x_axis:
        if x_axis.count('X') == 3:
            return f"Player 1 win"
        elif x_axis.count('O') == 3:
            return f"Player 2 win"
    return "Game is not finished"


get_game_table(game_table)
while True:
    error_code_x = add_x_to_table(table=game_table)
    while error_code_x > 0:
        if error_code_x == 1:
            print('Your choice is out of range')
            error_code_x = add_x_to_table(table=game_table)
        elif error_code_x == 2:
            print('Your choice location already have X or O ')
            error_code_x = add_x_to_table(table=game_table)
    message = who_win(table=game_table)
    print(message)
    if message == "Game is not finished":
        pass
    else:
        break
    error_code_y = add_o_to_table(table=game_table)
    while error_code_y > 0:
        if error_code_y == 1:
            print('Your choice is out of range')
            error_code_y = add_o_to_table(table=game_table)
        elif error_code_y == 2:
            print('Your choice location already have X or O ')
            error_code_y = add_o_to_table(table=game_table)
    message = who_win(game_table)
    print(message)
    if message == "Game is not finished":
        pass
    else:
        break