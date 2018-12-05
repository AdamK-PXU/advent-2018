import sys

filename = "input.txt"

with open(filename) as f:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    polymer = f.readlines()
    originalPolymer = polymer[0].strip()

    for i in range(len(alphabet)):
        polymer = originalPolymer
        adjustedPolymer = ''
        encounteredReaction = True

        for j in range(len(polymer)):
            if alphabet[i].upper() != polymer[j].upper():
                adjustedPolymer += polymer[j]

        polymer = adjustedPolymer
        reducedPolymer = []

        for c in polymer:
            if len(reducedPolymer) > 0 and reducedPolymer[-1].upper() == c.upper():
                if reducedPolymer[-1].isupper() and c.isupper() != True:
                    reducedPolymer.pop()
                elif reducedPolymer[-1].isupper() != True and c.isupper():
                    reducedPolymer.pop()
                else:
                    reducedPolymer.append(c)
            else:
                reducedPolymer.append(c)

        alphabet[i] = len(reducedPolymer)

    shortestPolymerSize = sys.maxsize
    shortestPolymerIndex = -1

    for i in range(len(alphabet)):
        if alphabet[i] < shortestPolymerSize:
            shortestPolymerIndex = i
            shortestPolymerSize = alphabet[i]

    print shortestPolymerSize
