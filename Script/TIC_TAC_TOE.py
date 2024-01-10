from collections import deque

turn = deque(["X", "O"])

board = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"],
]


def change_turn():
    turn.rotate()
    return turn[0]


def print_board(board):
    # Loop over each row
    for row in board:
        # Convert each element to a string and join with spaces
        print(' '.join(map(str, row)))


def capture():
    row = ""
    column = ""
    while row == "" and column == "":
        option = input("Player {}, insert the position (row,column) from 1 to 3. 'exit' to exit: ".format(turn[0]))
        if option == "exit":
            exit()

        try:
            row, column = option.split(",")
            try:
                row = int(row)
                column = int(column)
                if row >= 4 or column >= 4:
                    print("Values for row and/or column not valids")
                else:
                    return row, column
            except Exception as e:
                print("Values no valids")
        except Exception as e:
            print("Option not valid: ", e)
        row = ""
        column = ""

def write(row, column):
    if verify():
        board[row-1][column-1] = turn[0]
    else:
        print("The space is already occupied. Please try again")
        change_turn()


def verify():
    if board[row-1][column-1] == "*":
        return True
    else:
        return False


def verify_win(board, flag):
    if (((board[0][0] == turn[0]) and (board[0][1] == turn[0]) and (board[0][2] == turn[0])) or
            ((board[0][0] == turn[0]) and (board[1][0] == turn[0]) and (board[2][0] == turn[0])) or
            ((board[1][0] == turn[0]) and (board[1][1] == turn[0]) and (board[1][2] == turn[0])) or
            ((board[0][1] == turn[0]) and (board[1][1] == turn[0]) and (board[2][1] == turn[0])) or
            ((board[2][0] == turn[0]) and (board[2][1] == turn[0]) and (board[2][2] == turn[0])) or
            ((board[0][2] == turn[0]) and (board[1][2] == turn[0]) and (board[2][2] == turn[0])) or
            ((board[0][0] == turn[0]) and (board[1][1] == turn[0]) and (board[2][2] == turn[0])) or
            ((board[0][2] == turn[0]) and (board[1][1] == turn[0]) and (board[2][0] == turn[0]))):
        print_board(board)
        print("Player {} YOU WON".format(turn[0]))
        flag = False
    return flag


if __name__ == "__main__":
    flag = True
    while flag:
        print_board(board)
        row, column = capture()
        write(row, column)
        flag = verify_win(board, flag)
        change_turn()