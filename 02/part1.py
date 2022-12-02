# A = Rock      X = Rock
# B = Paper     Y = Paper
# C = Scissors  Z = Scissors

# Rock 1p       Lose 0p
# Paper 2p      Draw 3p
# Scissors 3p   Win 6p

# Score per round = Shape + Outcome

def translateShape(shape):
    if shape == 'X':
        return 'A'
    elif shape == 'Y':
        return 'B'
    elif shape == 'Z':
        return 'C'

def getPointsForOutcome(opponentShape, myShape):
    if opponentShape == myShape:
        return 3
    elif opponentShape == 'A' and myShape == 'B':
        return 6
    elif opponentShape == 'A' and myShape == 'C':
        return 0
    elif opponentShape == 'B' and myShape == 'A':
        return 0
    elif opponentShape == 'B' and myShape == 'C':
        return 6
    elif opponentShape == 'C' and myShape == 'A':
        return 6
    elif opponentShape == 'C' and myShape == 'B':
        return 0

def getPointsForShape(myShape):
    if myShape == 'A':
        return 1
    elif myShape == 'B':
        return 2
    elif myShape == 'C':
        return 3

file = open('input.txt', 'r')

totalPoints = 0

for line in file:
    opponentShape, myShape = line.split();
    myTranslatedShape = translateShape(myShape)

    pointsForThisOutcome = getPointsForOutcome(opponentShape, myTranslatedShape)
    pointsForThisShape = getPointsForShape(myTranslatedShape)

    totalPoints += pointsForThisOutcome + pointsForThisShape

# answer to part 1
print('totalPoints: ' + str(totalPoints))