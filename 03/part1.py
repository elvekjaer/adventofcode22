def getDuplicateItem(allItems):
    allItemsList = [*allItems.rstrip()]

    compartmentA = allItemsList[:len(allItemsList)//2]
    compartmentB = allItemsList[len(allItemsList)//2:]

    setA = set(compartmentA)
    setB = set(compartmentB)

    sharedItem = setA.intersection(setB)

    return list(sharedItem)[0]

def getPriorityForItem(item):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabetList = [*alphabet]

    return alphabetList.index(item) + 1

rucksack = open('input.txt', 'r')

totalPriority = 0

for items in rucksack:
    duplicateItem = getDuplicateItem(items)
    priority = getPriorityForItem(duplicateItem)
    totalPriority += priority

# answer to part 1
print(totalPriority)