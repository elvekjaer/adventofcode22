# A = Rock      X = Lose
# B = Paper     Y = Draw
# C = Scissors  Z = Win

# Rock 1p       Lose 0p
# Paper 2p      Draw 3p
# Scissors 3p   Win 6p

# Score per round = Shape + Outcome

class Shape:
    def __init__(self, losesAgainst, drawAgainst, winsAgainst, points):
        self.losesAgainst = losesAgainst
        self.drawAgainst = drawAgainst
        self.winsAgainst = winsAgainst
        self.points = points

class Rock (Shape):
    def __init__(self):
        super().__init__('B', 'A', 'C', 1)

class Paper (Shape):
    def __init__(self):
        super().__init__('C', 'B', 'A', 2)

class Scissors (Shape):
    def __init__(self):
        super().__init__('A', 'C', 'B', 3)

def getShapeObj(shape: str):
    if shape == 'A':
        return Rock()
    elif shape == 'B':
        return Paper()
    elif shape == 'C':
        return Scissors()

def getSelectionByDesiredResult(opponentShape: Shape, desiredResult: str):
    if desiredResult == 'X':
        return opponentShape.winsAgainst
    elif desiredResult == 'Y':
        return opponentShape.drawAgainst
    elif desiredResult == 'Z':
        return opponentShape.losesAgainst

def getPointsForResult(result):
    if result == 'X':
        return 0
    elif result == 'Y':
        return 3
    elif result == 'Z':
        return 6

file = open('input.txt', 'r')

totalPoints = 0

for line in file:
    opponentSelection, desiredResult = line.split();

    opponentShape = getShapeObj(opponentSelection)
    myShape = getShapeObj(getSelectionByDesiredResult(opponentShape, desiredResult))

    pointsForThisOutcome = getPointsForResult(desiredResult)
    pointsForThisShape = myShape.points

    totalPoints += pointsForThisOutcome + pointsForThisShape

# answer to part 2
print('totalPoints: ' + str(totalPoints))