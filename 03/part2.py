def getSharedItem(rucksackA: list, rucksackB: list, rucksackC: list):
    sharedItem = set(rucksackA).intersection(set(rucksackB)).intersection(set(rucksackC))

    return list(sharedItem)[0]

def getPriorityForItem(item):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabetList = [*alphabet]

    return alphabetList.index(item) + 1


rucksack = open('input.txt', 'r')

totalPriority = 0
counter = 0

rucksackA = []
rucksackB = []
rucksackC = []

for items in rucksack:

    if counter == 0:
        rucksackA = [*items.rstrip()]
    elif counter == 1:
        rucksackB = [*items.rstrip()]
    elif counter == 2:
        rucksackC = [*items.rstrip()]
    
    if counter == 2:
        sharedItem = getSharedItem(rucksackA, rucksackB, rucksackC)
        priority = getPriorityForItem(sharedItem)
        totalPriority += priority
        counter = 0
    else:
        counter += 1

# answer to part 2
print(totalPriority)