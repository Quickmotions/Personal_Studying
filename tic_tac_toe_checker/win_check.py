def is_solved(board):
    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    player_1 = []
    player_2 = []
    empty = False

    index = 1

    for row in board:
        for item in row:
            if item == 0:
                empty = True
            elif item == 1:
                player_1.append(index)
            elif item == 2:
                player_2.append(index)
            index += 1

    for row in soln:

        for x in row:
            if x not in player_1:
                break
        else:
            return 1

        for x in row:
            if x not in player_2:
                break
        else:
            return 2

    if empty is True:
        return -1
    else:
        return 0



# not yet finished
board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]
print(is_solved(board))

# winning row
board = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]
print(is_solved(board))

# winning column
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
print(is_solved(board))

# draw
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]
print(is_solved(board))


