from collections import deque

turn = deque(["X", "O"])

board = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"],
]


def cambiar_turno():
    turn.rotate()
    return turn[0]


def print_board(board):
    # Loop over each row
    for row in board:
        # Convert each element to a string and join with spaces
        print(' '.join(map(str, row)))


def capturar():
    row = ""
    column = ""
    while row == "" and column == "":
        option = input("Jugador {}, ingrese la posición (fila,coluumna) de 1 a 3. 'salir' para salir: ".format(turn[0]))
        if option == "salir":
            exit()

        try:
            row, column = option.split(",")
            try:
                row = int(row)
                column = int(column)
                if row >= 4 or column >= 4:
                    print("Valores para fila y/o columna no validos")
                else:
                    return row, column
            except Exception as e:
                print("Valores no validos")
        except Exception as e:
            print("Opción no valida: ", e)
        row = ""
        column = ""

def write(row, column):
    if verify():
        board[row-1][column-1] = turn[0]
    else:
        print("No se pudó, intente de nuevo")
        cambiar_turno()


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
        row, column = capturar()
        write(row, column)
        flag = verify_win(board, flag)
        cambiar_turno()