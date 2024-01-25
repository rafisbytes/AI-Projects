import time
import random
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
    visitedBoards = []
    st = time.time()
    while True:
        if len(visitedBoards) > 30:
            visitedBoards.pop(0)
        currentScore = scoreBoard(currentBoard)
        visitedBoards.append(currentBoard)
        currentNeighbors = []
        for row1 in range(8):
            for row2 in range(8):
                newBoard = swichRows(currentBoard, row1, row2)
                if newBoard not in visitedBoards:
                    currentNeighbors.append(newBoard)
        if currentNeighbors == []:
            return "Didn't word"
        else:
            randomNumber = random.choice(range(len(currentNeighbors)))
        for board in currentNeighbors:
            score = scoreBoard(board)
            if score < currentScore:
                currentBoard = formatBoard(board)
                if score == 0:
                    return currentBoard
                continue
        currentBoard = formatBoard(currentNeighbors[randomNumber])

print(make8qweensBoard())
