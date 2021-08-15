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
    x_count = 0
    o_count = 0
    for row in board:
        for col in row:
            if(col == X):
                x_count += 1
            elif(col == O):
                o_count += 1
    current_turn = X
    if(x_count>o_count):
        current_turn = O
    return current_turn


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if(board[i][j]==EMPTY):
                actions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    i,j = action
    if(board_copy[i][j]!=EMPTY):
        print("invalid action",board,action)
        raise Exception
    board_copy[i][j] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if(board[i][0]==board[i][1]==board[i][2] and board[i][0]!=EMPTY):
            return board[i][0]
        if(board[0][i]==board[1][i]==board[2][i] and board[0][i]!=EMPTY):
            return board[0][i]
    if(((board[0][0]==board[1][1]==board[2][2]) or (board[0][2]==board[1][1]==board[2][0])) and board[1][1]!=EMPTY):
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board)):
        return True
    for i in range(3):
        for j in range(3):
            if(board[i][j]==EMPTY):
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    tmp = winner(board)
    return 1 if(tmp==X) else -1 if(tmp==O) else 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #Adding alpha beta pruning is pending
    if(player(board)==X):
        v,action =  max_value(board)
        return action
    else:
        v,action =  min_value(board)
        return action

def max_value(board):
    if(terminal(board)):
        return utility(board), None
    v= -2
    selected_action = None
    for a in actions(board):
        tmp, next_action = min_value(result(board,a))
        if(tmp>v):
            v= tmp
            selected_action = a
        if(v==1):
            return v, selected_action
    return v, selected_action

def min_value(board):
    if(terminal(board)):
        return utility(board), None
    v= 2
    selected_action = None
    for a in actions(board):
        tmp, next_action = max_value(result(board,a))
        if(tmp<v):
            v= tmp
            selected_action = a
        if(v==-1):
            return v, selected_action
    return v, selected_action

