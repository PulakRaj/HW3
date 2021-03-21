import copy
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
                    if (row + i*x == len(state)) or (column + i*y == len(state)):
                        break
                    elif state[row + i*x][column + i*y] == other:
                        counter += 1
                    elif state[row + i*x][column + i*y] == player:
                        flipped += counter
                    else:
                        break
    return flipped


# state = [[' ', ' ', ' ', ' '], [' ', 'W', 'W', ' '], ['B', 'B', 'B', ' '], [' ', ' ', ' ', ' ']]
# for i in state:
#     print(i)
# print(get_move_value(state, "B", 0, 1))

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
                    if (row + i*x == len(state)) or (column + i*y == len(state)):
                        break
                    elif state[row + i*x][column + i*y] == other:
                        flips.append((row + i*x, column + i*y))
                    elif state[row + i*x][column + i*y] == player:
                        for position in flips:
                            new_state[position[0]][position[1]] = player
                    else:
                        break
    new_state[row][column] = player
    return new_state

state = [[' ', ' ', ' ', ' '], [' ', 'W', 'W', ' '], ['B', 'B', 'B', ' '], [' ', ' ', ' ', ' ']]
newstate = execute_move(state, "B", 0, 2)
for i in state:
    print(i)
print("")
for i in newstate:
    print(i)


"""
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)

"""


def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    # Your implementation goes here
    return (blackpieces, whitepieces)


"""
Check whether a state is a terminal state. 
"""


def is_terminal_state(state, state_list=None):
    terminal = True
    for i in range(len(state)):
        for j in range(len(state)):
            if get_move_value(state, "W", i, j) != 0:
                terminal = False
            if get_move_value(state, "B", i, j) != 0:
                terminal = False
    return terminal

print(is_terminal_state(newstate))

"""
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
"""


def minimax(state, player):
    value = 0
    row = -1
    column = -1
    # Your implementation goes here
    return (value, row, column)


"""
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
"""


def full_minimax(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here
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
    # Your implementation goes here
    return (value, row, column)


"""
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
"""


def full_minimax_ab(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here
    return (value, move_sequence)
