FINISH_POSITION = (("1", "2", "3"),
                   ("4", "5", "6"),
                   ("7", "8", " "))

def makeToArray(myTuple):
    newArray = []
    for Ituple in myTuple:
        newArray.append(list(Ituple))
    return newArray

def makeToTuple(array):
    arrayOfTuple = []
    for Iarray in array:
        arrayOfTuple.append(tuple(Iarray))
    return tuple(arrayOfTuple)



def findEmptyLocation(game):
    for y in range(3):
        for x in range(3):
            if game[y][x] == " ": return [x, y]

def findPossibleMoves(game):
    emptyLocation = findEmptyLocation(game)
    possibleMoves = []
    if emptyLocation[0] > 0:
        possibleMoves.append("R")
    if emptyLocation[0] < 2:
        possibleMoves.append("L")
    if emptyLocation[1] > 0:
        possibleMoves.append("D")
    if emptyLocation[1] < 2:
        possibleMoves.append("U")
    return possibleMoves

def makeMove(game, move):
    newGame = makeToArray(game)
    el = findEmptyLocation(newGame)
    if move == "R":
        moveNumber = newGame[el[1]][el[0] - 1]
        newGame[el[1]][el[0]] = moveNumber
        newGame[el[1]][el[0] - 1] = " "
    elif move == "L":
        moveNumber = newGame[el[1]][el[0] + 1]
        newGame[el[1]][el[0]] = moveNumber
        newGame[el[1]][el[0] + 1] = " "
    elif move == "D":
        moveNumber = newGame[el[1] - 1][el[0]]
        newGame[el[1]][el[0]] = moveNumber
        newGame[el[1] - 1][el[0]] = " "
    elif move == "U":
        moveNumber = newGame[el[1] + 1][el[0]]
        newGame[el[1]][el[0]] = moveNumber
        newGame[el[1] + 1][el[0]] = " "
    return makeToTuple(newGame)

def getSolution(game):
    possibleGames = [game]
    visitedGames = []
    pred = {}
    prevMove = {}
    while possibleGames != []:
        currentGame = possibleGames.pop(0)
        if currentGame == FINISH_POSITION:
            break
        visitedGames.append(currentGame)
        possibleMoves = findPossibleMoves(currentGame)
        for move in possibleMoves:
            newGame = makeMove(currentGame, move)
            if newGame not in visitedGames:
                possibleGames.append(newGame)
                pred[newGame] = currentGame
                prevMove[newGame] = move
    if possibleGames != []:
        currentGame = FINISH_POSITION
        moveSolution = []
        while currentGame != game:
            moveSolution[:0] = [prevMove[currentGame]]
            currentGame = pred[currentGame]
        return moveSolution
    else:
        print("No solution")

print(getSolution((
    ("2", "6", "3"),
    ("1", "7", "8"),
    ("4", "5", " ")
)))
