import sys

filename = "input.txt"

with open(filename) as f:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    polymer = f.readlines()
    originalPolymer = polymer[0]

    for i in range(len(alphabet)):
        polymer = originalPolymer
        adjustedPolymer = ''
        encounteredReaction = True

        for j in range(len(polymer)):
            if alphabet[i].upper() != polymer[j].upper():
                adjustedPolymer += polymer[j]

        polymer = adjustedPolymer

        while encounteredReaction:
            reactedPolymer = ''
            encounteredReaction = False

            for j in range(len(polymer) - 1):
                c1 = polymer[j]
                c2 = polymer[j + 1]

                if c1.upper() == c2.upper():
                    if c1.isupper() and c2.isupper() != True:
                        reactedPolymer += polymer[(j + 2):]
                        encounteredReaction = True
                        break
                    elif c1.isupper() != True and c2.isupper():
                        reactedPolymer += polymer[(j + 2):]
                        encounteredReaction = True
                        break
                    else:
                        reactedPolymer += c1
                else:
                    reactedPolymer += c1

            polymer = reactedPolymer

        alphabet[i] = len(polymer)

    shortestPolymerSize = sys.maxsize
    shortestPolymerIndex = -1

    for i in range(len(alphabet)):
        if alphabet[i] < shortestPolymerSize:
            shortestPolymerIndex = i
            shortestPolymerSize = alphabet[i]

    print shortestPolymerSize
