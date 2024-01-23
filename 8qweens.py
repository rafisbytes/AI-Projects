import time

def checkBoard(board):
    for q in range(len(board)):
        for compQ in range(q + 1, len(board)):
            if board[q][0] == board[compQ][0] or \
            board[q][1] == board[compQ][1] or \
            board[q][0] + board[q][1] == board[compQ][0] + board[compQ][1] or \
            board[q][0] - board[q][1] == board[compQ][0] - board[compQ][1]:
                return False
    return True

def emptySpaces(board):
    spaces = []
    for x in range(1, 9):
        for y in range(1, 9):
            if [x, y] not in board:
                spaces.append([x, y])
    return spaces

def formatBoard(board):
    newBoard = []
    for i in range(1, 9):
        newElements = list(filter(lambda x: x[0] == i, board))
        newBoard += newElements
    return newBoard

def make8qweensBoardFrom4(board):
    possibleBoards = [board]
    visitedBoards = []
    while True:
        if possibleBoards == []:
            return
        currentBoard = possibleBoards[0]
        possibleBoards.pop(0)
        visitedBoards.append(currentBoard)
        for newSpace in emptySpaces(currentBoard):
            newBoard = formatBoard(currentBoard + [newSpace])
            if newBoard not in visitedBoards and checkBoard(newBoard):
                if len(newBoard) == 8:
                    return newBoard
                else:
                    possibleBoards.append(newBoard)


def make8qweensBoard(switch, lenthofResult):
    possibleBoards = [[]]
    visitedBoards = []
    goodBoards = []
    print("Speed:")
    st = time.time()
    while True:
        currentBoard = possibleBoards[len(possibleBoards) - 1]
        print("-", end="", flush=True)
        possibleBoards.pop(len(possibleBoards) - 1)
        visitedBoards.append(currentBoard)
        for newSpace in emptySpaces(currentBoard):
            newBoard = formatBoard(currentBoard + [newSpace])
            if newBoard not in visitedBoards and checkBoard(newBoard):
                if len(newBoard) == switch:
                    tryNewBoard = make8qweensBoardFrom4(newBoard)
                    if tryNewBoard and tryNewBoard not in goodBoards:
                        goodBoards.append(tryNewBoard)
                        et = time.time()
                        print("\n Found solution. Time: ", et - st)
                        st = et
                        if len(goodBoards) == lenthofResult:
                            return goodBoards
                else:
                    possibleBoards.append(newBoard)

print(make8qweensBoard(5, int(input("How many solutions do you want to find?"))))
