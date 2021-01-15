#Mancala game
#Rules: 6x2 board + one wide one on either side
#Total of 48 marbles
#Play around the board, rotating into the screen/clockwise
'''
Player 1: Left
Player 2: Right
        0    1    2    3    4    5
0     [   ][   ][   ][   ][   ][   ][   ]
1[   ][   ][   ][   ][   ][   ][   ]
'''
#board = [[4, 4, 4, 4, 4, 4, 0], [0, 4, 4, 4, 4, 4, 4]]




def draw_board(players = ["L", "R"], board = [[4, 4, 4, 4, 4, 4, 0], [0, 4, 4, 4, 4, 4, 4]]):
    if players[0] == "L":
        print("\nPlayer 1: Left")
        print("Player 2: Right")
    else:
        print("\nPlayer 1: Right")
        print("Player 2: Left")
    print("\n        0    1    2    3    4    5")
    for i in range(2):
        if i == 0:
            for x in range(len(board[i])):
                if x == 0:
                    if len(str(board[i][x])) == 1:
                        print("0     [ {} ]".format(board[i][x]), end = "")
                    else:
                        print("0     [ {}]".format(board[i][x]), end = "")
                else:
                    if len(str(board[i][x])) == 1:
                        print("[ {} ]".format(board[i][x]), end = "")
                    else:
                        print("[ {}]".format(board[i][x]), end = "")
        else:
            print()
            for x in range(len(board[i])):
                if x == 0:
                    if len(str(board[i][x])) == 1:
                        print("1[ {} ]".format(board[i][x]), end = "")
                    else:
                        print("1[ {}]".format(board[i][x]), end = "")
                else:
                    if len(str(board[i][x])) == 1:
                        print("[ {} ]".format(board[i][x]), end = "")
                    else:
                        print("[ {}]".format(board[i][x]), end = "")
    print("\n")


def input_player_side():
    choose = input("Choose which side Player 1 is: (Enter 'L' for Left side, or 'R' for Right side)\n").capitalize()
    if choose == "L":
        return ["L", "R"]
    elif choose == "R":
        return ["R", "L"]
    else:
        input_player_side()


def make_move_step(board, side: str, row: int, col: int, marbles_in_hand: int):
    print(marbles_in_hand)
    draw_board(["L", "R"], board)
    if side == "L":
        if marbles_in_hand > 0:
            if row == 0:
                if col == 5:
                    board[1][6] += 1
                    return make_move_step(board, side, 1, 6, marbles_in_hand - 1)
                else:
                    col += 1
                    board[row][col] += 1
                    return make_move_step(board, side, row, col, marbles_in_hand - 1)
            else:
                if col == 0:
                    board[0][0] += 1
                    return make_move_step(board, side, 0, 0, marbles_in_hand - 1)
                else:
                    col -=1
                    board[row][col] += 1
                    return make_move_step(board, side, row, col, marbles_in_hand - 1)
        else:
            if row == 0:
                return 0, col
            else:
                if col == 6:
                    return 0, 5
                else:
                    return 1, col

                
    elif side == "R":
        if marbles_in_hand > 0:
            if row == 0:
                if col == 6:
                    board[1][6] += 1
                    return make_move_step(board, side, 1, 6, marbles_in_hand - 1)
                else:
                    col += 1
                    board[row][col] += 1
                    return make_move_step(board, side, row, col, marbles_in_hand - 1)
            else:
                if col == 1:
                    board[0][0] += 1
                    return make_move_step(board, side, 0, 0, marbles_in_hand - 1)
                else:
                    col -=1
                    board[row][col] += 1
                    return make_move_step(board, side, row, col, marbles_in_hand - 1)
        else:
            if row == 0:
                if col == 0:
                    return 1, 1
                else:
                    return 0, col
            else:
                return 1, col


def make_move_full(board, side: str, row: int, col: int, marbles_in_hand: int) -> bool:#Returns True if the player goes again, else returns False
    final_row, final_col = make_move_step(board, side, row, col, marbles_in_hand)
    if side == "L" and final_row == 1 and final_col == 0:
        return True
    elif side == "R" and final_row == 0 and final_col == 6:
        return True
    elif board[final_row][final_col] > 1:
        marbles_in_hand = board[final_row][final_col]
        board[final_row][final_col] = 0
        return make_move_full(board, side, final_row, final_col, marbles_in_hand)
    else:
        return False


def make_move(board, players, side: str):
    if side == players[0]:
        move_list = input('Player 1, choose a space: (Type in the format "Row Column")\n').split()
        row = int(move_list[0])
        col = int(move_list[1])
        if row == 1:
            col += 1
        marbles_in_hand = board[row][col]
        board[row][col] = 0
        go_again = make_move_full(board, side, row, col, marbles_in_hand)
        draw_board(players, board)
        while go_again:
            move_list = input('Player 1, choose another space: (Type in the format "Row Column")\n').split()
            row = int(move_list[0])
            col = int(move_list[1])
            if row == 1:
                col += 1
            marbles_in_hand = board[row][col]
            board[row][col] = 0
            go_again = make_move_full(board, side, row, col, marbles_in_hand)
            draw_board(players, board)
    else:
        move_list = input('Player 2, choose a space: (Type in the format "Row Column")\n').split()
        row = int(move_list[0])
        col = int(move_list[1])
        if row == 1:
            col += 1
        marbles_in_hand = board[row][col]
        board[row][col] = 0
        go_again = make_move_full(board, side, row, col, marbles_in_hand)
        draw_board(players, board)
        while go_again:
            move_list = input('Player 2, choose another space: (Type in the format "Row Column")\n').split()
            row = int(move_list[0])
            col = int(move_list[1])
            if row == 1:
                col += 1
            marbles_in_hand = board[row][col]
            board[row][col] = 0
            go_again = make_move_full(board, side, row, col, marbles_in_hand)
            draw_board(players, board)


def is_board_empty(board) -> bool:
    if board[1][0] + board[0][6] == 48:
        return True
    else:
        return False


#Main:
players = input_player_side()
board = [[4, 4, 4, 4, 4, 4, 0], [0, 4, 4, 4, 4, 4, 4]]
turn = 0
while not(is_board_empty(board)):
    if turn % 2 == 0:
        side = players[0]
    else:
        side = players[1]
    draw_board(players, board)
    make_move(board, players, side)
    turn += 1
if board[1][0] == board[0][6]:
    print("Tie!")
elif board[1][0] > board[0][6]:
    winner = players.index("L") + 1
elif board[1][0] < board[0][6]:
    winner = players.index("R") + 1
print("Congrats Player {}, You Win!".format(winner))
