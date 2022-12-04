campSections = open('input.txt', 'r')

def getAllSectionNumbersList(sections):
    startIndex, stopIndex = sections.split('-')

    return list(range(int(startIndex), int(stopIndex) + 1))

def isAllItemsOverlapping(rangeA, rangeB):
    for item in rangeA:
        if item in rangeB:
            continue
        return False

    return True

def isAnyItemOverlapping(rangeA, rangeB):
    for item in rangeA:
        if item in rangeB:
            return True

    return False

allItemsOverlappingPairs = 0
anyItemsOverlappingPairs = 0

for line in campSections:

    sectionA, sectionB = line.rstrip().split(',')

    sectionANumbers = getAllSectionNumbersList(sectionA)
    sectionBNumbers = getAllSectionNumbersList(sectionB)

    isACompletelyOverlappingB = isAllItemsOverlapping(sectionANumbers, sectionBNumbers)
    isBCompletelyOverlappingA = isAllItemsOverlapping(sectionBNumbers, sectionANumbers)

    isAOverlappingAnyB = isAnyItemOverlapping(sectionANumbers, sectionBNumbers)
    isBOverlappingAnyA = isAnyItemOverlapping(sectionBNumbers, sectionANumbers)

    if isACompletelyOverlappingB or isBCompletelyOverlappingA:
        allItemsOverlappingPairs += 1
    
    if isAOverlappingAnyB or isBOverlappingAnyA:
        anyItemsOverlappingPairs += 1

# answer to part 1
print(allItemsOverlappingPairs)

# answer to part 2
print(anyItemsOverlappingPairs)