tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

for i in tic_tac_toe_board:
    for j in i:
        print(j, end=' ')
    print()