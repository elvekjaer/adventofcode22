with open('input.txt') as f:
    content = f.readlines()
    veryLongCharacterString = content[0]

    characters = [character for character in veryLongCharacterString]

    lastCharacters = []
    counter = 0

    threshold = 4

    for character in characters:
        if character not in lastCharacters and len(lastCharacters) == threshold:
            print(counter)
            break
        elif character not in lastCharacters and len(lastCharacters) < threshold:
            lastCharacters.append(character)
        elif character in lastCharacters:
            indexOfExistingCharacter = lastCharacters.index(character)
            lastCharacters = lastCharacters[indexOfExistingCharacter + 1:]
            lastCharacters.append(character)
        
        counter += 1