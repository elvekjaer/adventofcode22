file = open('input.txt', 'r')

totalCaloriesPerElf = []

totalCarriedByCurrentElf = 0;

for line in file:

    if line != '\n':
        calories = line.rstrip()
        totalCarriedByCurrentElf += int(calories)
    else:
        totalCaloriesPerElf.append(totalCarriedByCurrentElf)
        totalCarriedByCurrentElf = 0

mostCaloriesCarriedByOneElf = max(totalCaloriesPerElf)

# answer to part 1
print('mostCaloriesCarriedByOneElf: ' + str(mostCaloriesCarriedByOneElf))

topThreeCalories = sorted(totalCaloriesPerElf, reverse=True)[:3]

topThreeCaloriesTotal = 0
for calories in topThreeCalories:
    topThreeCaloriesTotal += calories

# answer to part 2
print('topThreeCaloriesTotal: ' + str(topThreeCaloriesTotal))