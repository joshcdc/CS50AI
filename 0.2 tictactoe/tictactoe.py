"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    balance = 0

    for i in board:
        for j in i:
            if j == X:
                balance += 1
            elif j == O:
                balance -= 1
    
    if balance == 1:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for j in range(3):
        for i in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Invalid Action")
    x,y = action

    newBoard = copy.deepcopy(board)
    newBoard[x][y] = player(board)
    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check horizontal and vertical
  
    for j in [X, O]:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == j:
                return j
            elif board[0][i] == board[1][i] == board[2][i] == j:
                return j
        
            if board[0][0] == board[1][1] == board[2][2] == j:
                return j
            elif board[0][2] == board[1][1] == board[2][0] == j:
                return j
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """ 
    if terminal(board):
        return None
    elif player(board) == X:
        allActions = []
        allCosts = []
        for i in actions(board):
            allActions.append(i)
            allCosts.append(minVal(result(board, i)))
        return allActions[allCosts.index(max(allCosts))]
    elif player(board) == O:
        allActions = []
        allCosts = []
        for i in actions(board):
            allActions.append(i)
            allCosts.append(maxVal(result(board, i)))
        return allActions[allCosts.index(min(allCosts))]
            
            

def maxVal(board):
    if terminal(board):
        return utility(board)
    v = -2
    for i in actions(board):
        v = max(v, minVal(result(board,i)))
    return v

def minVal(board):
    if terminal(board):
        return utility(board)
    v = 2
    for i in actions(board):
        v = min(v, maxVal(result(board,i)))
    return v