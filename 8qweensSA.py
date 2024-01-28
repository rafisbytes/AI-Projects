import random
import math
STARTING_BOARD = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]

def checkBoard(board):
    for q in range(len(board)):
        for compQ in range(q + 1, len(board)):
            if board[q][0] == board[compQ][0] or \
            board[q][1] == board[compQ][1] or \
            board[q][0] + board[q][1] == board[compQ][0] + board[compQ][1] or \
            board[q][0] - board[q][1] == board[compQ][0] - board[compQ][1]:
                return False
    return True

def formatBoard(board):
    newBoard = []
    for i in range(1, 9):
        newElements = list(filter(lambda x: x[0] == i, board))
        newBoard += newElements
    return newBoard

def scoreBoard(board):
    score = 0
    for q in range(len(board)):
        for compQ in range(q + 1, len(board)):
            if board[q][0] + board[q][1] == board[compQ][0] + board[compQ][1] or \
            board[q][0] - board[q][1] == board[compQ][0] - board[compQ][1]:
                score += 1
    return score

def swichRows(board, row1, row2):
    newBoard = []
    for row in range(8):
        if row == row1:
            newBoard.append([board[row2][0], board[row1][1]])
        elif row == row2:
            newBoard.append([board[row1][0], board[row2][1]])
        else:
            newBoard.append(board[row])
    return newBoard

def make8qweensBoard():
    currentBoard = STARTING_BOARD.copy()
    bestBoard = STARTING_BOARD.copy()
    temp = temp0 = 1.5
    t = 1
    while scoreBoard(bestBoard) != 0:
        nextBoard = swichRows(currentBoard, *random.sample(range(8), 2))
        lossDiffernce = scoreBoard(nextBoard) - scoreBoard(currentBoard)
        probability = min(1, math.exp(-lossDiffernce/temp))
        if random.random() < probability:
            currentBoard = nextBoard
        if scoreBoard(currentBoard) < scoreBoard(bestBoard):
            bestBoard = currentBoard
        t = t + 1
        temp = temp0 / math.log(t + 1)
    return bestBoard
print(make8qweensBoard())
