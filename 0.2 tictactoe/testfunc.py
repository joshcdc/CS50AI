from tictactoe import * # type: ignore

board = initial_state()

board = result(board, (2,0))
board = result(board, (0,1))
board = result(board, (2,1))
board = result(board, (0,2))
board = result(board, (2,2))

print(board)
print(terminal(board))
print(winner(board))
