filename = "input.txt"

with open(filename) as f:
    polymer = f.readlines()
    polymer = polymer[0]
    encounteredReaction = True

    while encounteredReaction:
        reactedPolymer = ''
        encounteredReaction = False

        for i in range(len(polymer) - 1):
            c1 = polymer[i]
            c2 = polymer[i + 1]

            if c1.upper() == c2.upper():
                if c1.isupper() and c2.isupper() != True:
                    reactedPolymer += polymer[(i + 2):]
                    encounteredReaction = True
                    break
                elif c1.isupper() != True and c2.isupper():
                    reactedPolymer += polymer[(i + 2):]
                    encounteredReaction = True
                    break
                else:
                    reactedPolymer += c1
            else:
                reactedPolymer += c1

        polymer = reactedPolymer

    print len(polymer)
