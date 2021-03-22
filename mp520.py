"""
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
"""


def get_move_value(state, player, row, column):
    flipped = 0
    if player == "W":
        other = "B"
    else:
        other = "W"
    increments = [0, 1,-1]
    for x in increments:
        for y in increments:
            if x == 0 and y == 0:
                pass
            else:
                counter = 0
                for i in range(1, len(state)):
                    if (row + i*x == len(state)) or (column + i*y == len(state)) or (row + i*x < 0) or (column + i*y < 0):
                        break
                    elif state[row + i*x][column + i*y] == other:
                        counter += 1
                    elif state[row + i*x][column + i*y] == player:
                        flipped += counter
                        break
                    else:
                        break
    return flipped


"""
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
"""


def execute_move(state, player, row, column):
    new_state = [x[:] for x in state]
    flipped = 0
    if player == "W":
        other = "B"
    else:
        other = "W"
    increments = [0, 1,-1]
    for x in increments:
        for y in increments:
            if x == 0 and y == 0:
                pass
            else:
                flips = []
                for i in range(1, len(state)):
                    if (row + i*x == len(state)) or (column + i*y == len(state)) or (row + i*x < 0) or (column + i*y < 0):
                        break
                    elif state[row + i*x][column + i*y] == other:
                        flips.append((row + i*x, column + i*y))
                    elif state[row + i*x][column + i*y] == player:
                        for position in flips:
                            new_state[position[0]][position[1]] = player
                        break
                    else:
                        break
    new_state[row][column] = player
    return new_state


"""
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)

"""


def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == "B":
                blackpieces += 1
            if state[i][j] == "W":
                whitepieces += 1
    return (blackpieces, whitepieces)


"""
Check whether a state is a terminal state. 
"""


def is_terminal_state(state, state_list=None):
    terminal = True
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == " ":
                if get_move_value(state, "W", i, j) != 0:
                    return False
                if get_move_value(state, "B", i, j) != 0:
                    return False
    return terminal

"""
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
"""


def minimax(state, player):
    value = 0
    row = -1
    column = -1
    if (is_terminal_state(state)):
        scores = count_pieces(state)
        return (scores[0] - scores[1], row, column)
    def black():
        maxValue = -10000000
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] == " ":
                    if get_move_value(state, "B", i, j) > 0:
                        value = minimax(execute_move(state, "B", i, j), "W")[0]
                        if value > maxValue:
                            maxValue = value
                            row = i
                            column = j
        if maxValue == -10000000:
            return white()
        return (maxValue, row, column)
    def white():
        minValue = 10000000
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] == " ":
                    if get_move_value(state, "W", i, j) > 0:
                        value = minimax(execute_move(state, "W", i, j), "B")[0]
                        if value < minValue:
                            minValue = value
                            row = i
                            column = j
        if minValue == 10000000:
            return black()
        return (minValue, row, column)
    if player == "B":
        return black()
    if player == "W":
        return white()

"""
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
"""


def full_minimax(state, player):
    value = 0
    move_sequence = []
    while(is_terminal_state(state) == False):
        result = minimax(state, player)
        if get_move_value(state, player, result[1], result[2]) == 0:
            if player == "B":
                player = "W"
            elif player == "W":
                player = "B"
        move_sequence.append((player, result[1], result[2]))
        state = execute_move(state, player, result[1], result[2])
        if player == "B":
            player = "W"
        elif player == "W":
            player = "B"
    value = result[0]
    move_sequence.append((player,-1, -1))
    return (value, move_sequence)


"""
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
"""


def minimax_ab(state, player, alpha=-10000000, beta=10000000):
    value = 0
    row = -1
    column = -1
    if (is_terminal_state(state)):
        scores = count_pieces(state)
        return (scores[0] - scores[1], row, column)
    def black(alpha, beta):
        maxValue = -10000000
        flag = False
        for i in range(len(state)):
            if flag:
                break
            for j in range(len(state)):
                if state[i][j] == " ":
                    if get_move_value(state, "B", i, j) > 0:
                        value = minimax_ab(execute_move(state, "B", i, j), "W", alpha, beta)[0]
                        if value > maxValue:
                            maxValue = value
                            row = i
                            column = j
                        alpha = max(alpha, value)
                        if beta <= alpha:
                            flag = True
                            break
        if maxValue == -10000000:
            return white(alpha, beta)
        return (maxValue, row, column)
    def white(alpha, beta):
        flag = False
        minValue = 10000000
        for i in range(len(state)):
            if flag:
                break
            for j in range(len(state)):
                if state[i][j] == " ":
                    if get_move_value(state, "W", i, j) > 0:
                        value = minimax_ab(execute_move(state, "W", i, j), "B", alpha, beta)[0]
                        if value < minValue:
                            minValue = value
                            row = i
                            column = j
                        beta = min(beta, value)
                        if beta <= alpha:
                            flag = True
                            break
        if minValue == 10000000:
            return black(alpha, beta)
        return (minValue, row, column)
    if player == "B":
        return black(alpha, beta)
    if player == "W":
        return white(alpha, beta)

"""
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
"""


def full_minimax_ab(state, player):
    value = 0
    move_sequence = []
    while(is_terminal_state(state) == False):
        result = minimax_ab(state, player, alpha=-10000000, beta=10000000)
        if get_move_value(state, player, result[1], result[2]) == 0:
            if player == "B":
                player = "W"
            elif player == "W":
                player = "B"
        move_sequence.append((player, result[1], result[2]))
        state = execute_move(state, player, result[1], result[2])
        if player == "B":
            player = "W"
        elif player == "W":
            player = "B"
    value = result[0]
    move_sequence.append((player,-1, -1))
    return (value, move_sequence)