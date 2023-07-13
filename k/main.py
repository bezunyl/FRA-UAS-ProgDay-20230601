import sys

board = [x.rstrip().split() for x in sys.stdin.readlines()]

def straight_win(board):
    for hori in board:
        rowset = set(hori)
        if len(rowset) == 1:
            if list(rowset)[0] == "X":
                print("Johan har vunnit")
                return True
            elif list(rowset)[0] == "O":
                print("Abdullah har vunnit")
                return True
    
    for i in range(3):
        vertset = set()

        for j in range(3):
            vertset.add(board[j][i])

        if len(vertset) == 1:
            if list(vertset)[0] == "X":
                print("Johan har vunnit")
                return True
            elif list(vertset)[0] == "O":
                print("Abdullah har vunnit")
                return True

    return False

def check_diagonal(board):
    dia1 = set([board[0][0], board[1][1], board[2][2]])
    dia2 = set([board[0][2], board[1][1], board[2][0]])

    if len(dia1) == 1:
        if list(dia1)[0] == "X":
            print("Johan har vunnit")
            return True
        elif list(dia1)[0] == "O":
            print("Abdullah har vunnit")
            return True

    if len(dia2) == 1:
        if list(dia2)[0] == "X":
            print("Johan har vunnit")
            return True
        elif list(dia2)[0] == "O":
            print("Abdullah har vunnit")
            return True

    return False

state = False

if not state:
    state = straight_win(board)

if not state:
    state = check_diagonal(board)

if not state:
    print("ingen har vunnit")
