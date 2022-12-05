#                 [B] [L]     [J]    
#             [B] [Q] [R]     [D] [T]
#             [G] [H] [H] [M] [N] [F]
#         [J] [N] [D] [F] [J] [H] [B]
#     [Q] [F] [W] [S] [V] [N] [F] [N]
# [W] [N] [H] [M] [L] [B] [R] [T] [Q]
# [L] [T] [C] [R] [R] [J] [W] [Z] [L]
# [S] [J] [S] [T] [T] [M] [D] [B] [H]
#  1   2   3   4   5   6   7   8   9 

stacks = {
    '1': ['S', 'L', 'W'],
    '2': ['J', 'T', 'N', 'Q'],
    '3': ['S', 'C', 'H', 'F', 'J'],
    '4': ['T', 'R', 'M', 'W', 'N', 'G', 'B'],
    '5': ['T', 'R', 'L', 'S', 'D', 'H', 'Q', 'B'],
    '6': ['M', 'J', 'B', 'V', 'F', 'H', 'R', 'L'],
    '7': ['D', 'W', 'R', 'N', 'J', 'M'],
    '8': ['B', 'Z', 'T', 'F', 'H', 'N', 'D', 'J'],
    '9': ['H', 'L', 'Q', 'N', 'B', 'F', 'T']
}

moveOrders = open('input.txt', 'r')

for order in moveOrders:
    # "move 5 from 4 to 5"
    orderList = order.rstrip().split()

    amountToMove = orderList[1]
    fromStack = stacks[orderList[3]]
    toStack = stacks[orderList[5]]

    for i in range(int(amountToMove)):
        if (len(fromStack) > 0):
            toStack.append(fromStack.pop())

topCrates = ''

for stack in stacks:
    topCrates += stacks[stack][-1]

# answer to part 1
print(topCrates)

