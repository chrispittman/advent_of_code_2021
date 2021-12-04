import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
draws = data[0].split(',')
data = data[1:]
num_boards = int((len(data)) / 6)
boards = [[] for i in range(num_boards)]
for i in range(num_boards):
    start_posn = i*6
    boards[i] = [line.split() for line in data[start_posn+1:start_posn+6]]

def get_solved_board(boards):
    for board in boards:
        if board_is_solved(board):
            return board
    return None

def board_is_solved(board):
    if board_row_is_solved(board):
       return True
    # transpose rows and colums
    trans_board = [[row[i] for row in board] for i in range(len(board[0]))]
    if board_row_is_solved(trans_board):
       return True
    return False

def board_row_is_solved(board):
    return ['x','x','x','x','x'] in board

def get_unmarked_cells(board):
    result = []
    for row in board:
        for cell in row:
            if cell != 'x':
                result.append(cell)
    return result

def mark_draw(board, draw):
    return [ [('x' if cell==draw else cell) for cell in row] for row in board]

for draw in draws:
    boards = [mark_draw(board, draw) for board in boards]
    solved_board = get_solved_board(boards)
    if solved_board:
       unmarked_cells = get_unmarked_cells(solved_board)
       sum_unmarked_cells = sum([int(c) for c in unmarked_cells])
       print(sum_unmarked_cells * int(draw))
       break
