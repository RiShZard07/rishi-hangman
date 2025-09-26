def show(grid):
    """Prints a tic tac toe grid"""
    print("+---+---+---+")
    for row in grid:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("+---+---+---+")
    '''
    Print grid like this:
    +---+---+---+
    | X |   |   |
    +---+---+---+
    | O | X | X |
    +---+---+---+
    | O |   |   |
    +---+---+---+
    '''

def won(grid, player):
    """Checks if player supplied ('X' or 'O') won the game
      If so, returns True, otherwise returns False"""
    for i in range(3):
        if grid[i][0] == player and grid[i][1] == player and grid[i][2] == player:
            return True
    for i in range(3):
        if grid[0][i] == player and grid[1][i] == player and grid[2][i] == player:
            return True
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True
    return False

def taken(grid, row, col):
    """Checks if the spot (row, col) on grid is available.
       Returns False if the spot on the grid is not taken,
       otherwise returns True"""
    if grid[row][col] == ' ':
        return False
    else:
        return True

def set_pos(grid, row, col, player):
    """Set a grid value at position row, col to player"""
    grid[row][col] = player

def read_pos(prompt):
    """Reads and returns a 0, 1, or 2 else forces a retry"""
    while True:
        try:
            value = int(input(prompt))
            if value == 0 or value == 1 or value == 2:
                return value
            else:
                print("Enter 0, 1, or 2")
        except:
            print("Enter 0, 1, or 2")


def main():
    """Implements a TicTacToe game"""
    grid = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
    player = 'X'
    i = 0
    # There will be 9 maximum turns
    while i < 9:
        show(grid)
        print('Player', player)
        row = read_pos('row: ')
        col = read_pos('col: ')
        # skip current iteration spot taken
        if taken(grid, row, col):
            print('Spot taken! Try again.')
            continue
        # set position
        set_pos(grid, row, col, player)
        # check if player has won
        if won(grid, player):
            show(grid)
            print('Player', player, 'wins!')
            exit()
        # switch players
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        i = i + 1
    # nobody won
    print('It is a draw!')

main()

"""
/Users/rishikeshavadamarla/PycharmProjects/PythonProject9/.venv/bin/python /Users/rishikeshavadamarla/PycharmProjects/PythonProject9/TicTacToe.py 
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player X
row: 0
col: 0
+---+---+---+
| X |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player O
row: 1
col: 1
+---+---+---+
| X |   |   |
+---+---+---+
|   | O |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player X
row: 1
col: 2
+---+---+---+
| X |   |   |
+---+---+---+
|   | O | X |
+---+---+---+
|   |   |   |
+---+---+---+
Player O
row: 0
col: 1
+---+---+---+
| X | O |   |
+---+---+---+
|   | O | X |
+---+---+---+
|   |   |   |
+---+---+---+
Player X
row: 1
col: 0
+---+---+---+
| X | O |   |
+---+---+---+
| X | O | X |
+---+---+---+
|   |   |   |
+---+---+---+
Player O
row: 2
col: 1
+---+---+---+
| X | O |   |
+---+---+---+
| X | O | X |
+---+---+---+
|   | O |   |
+---+---+---+
Player O wins!
"""

"""
/Users/rishikeshavadamarla/PycharmProjects/PythonProject9/.venv/bin/python /Users/rishikeshavadamarla/PycharmProjects/PythonProject9/TicTacToe.py 
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player X
row: 0
col: 0
+---+---+---+
| X |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player O
row: 0
col: 1
+---+---+---+
| X | O |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player X
row: 0
col: 2
+---+---+---+
| X | O | X |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player O
row: 1
col: 1
+---+---+---+
| X | O | X |
+---+---+---+
|   | O |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player X
row: 1
col: 2
+---+---+---+
| X | O | X |
+---+---+---+
|   | O | X |
+---+---+---+
|   |   |   |
+---+---+---+
Player O
row: 1
col: 1
Spot taken! Try again.
+---+---+---+
| X | O | X |
+---+---+---+
|   | O | X |
+---+---+---+
|   |   |   |
+---+---+---+
Player O
row: 1
col: 0
+---+---+---+
| X | O | X |
+---+---+---+
| O | O | X |
+---+---+---+
|   |   |   |
+---+---+---+
Player X
row: 2
col: 1
+---+---+---+
| X | O | X |
+---+---+---+
| O | O | X |
+---+---+---+
|   | X |   |
+---+---+---+
Player O
row: 2
col: 2
+---+---+---+
| X | O | X |
+---+---+---+
| O | O | X |
+---+---+---+
|   | X | O |
+---+---+---+
Player X
row: 2
col: 0
It is a draw!

Process finished with exit code 0
"""

"""
/Users/rishikeshavadamarla/PycharmProjects/PythonProject9/.venv/bin/python /Users/rishikeshavadamarla/PycharmProjects/PythonProject9/TicTacToe.py 
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player X
row: 1
col: 1
+---+---+---+
|   |   |   |
+---+---+---+
|   | X |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player O
row: 1
col: 1
Spot taken! Try again.
+---+---+---+
|   |   |   |
+---+---+---+
|   | X |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player O
row: abc
Enter 0, 1, or 2
row: -3
Enter 0, 1, or 2
row: 0
col: 0
+---+---+---+
| O |   |   |
+---+---+---+
|   | X |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player X
row: 0
col: 1
+---+---+---+
| O | X |   |
+---+---+---+
|   | X |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player O
row: 1
col: 0
+---+---+---+
| O | X |   |
+---+---+---+
| O | X |   |
+---+---+---+
|   |   |   |
+---+---+---+
Player X
row: 2
col: 1
+---+---+---+
| O | X |   |
+---+---+---+
| O | X |   |
+---+---+---+
|   | X |   |
+---+---+---+
Player X wins!

Process finished with exit code 0
"""