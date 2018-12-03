import string

filename = "input.txt"

def getLines(f):
    lines = []
    line = f.readline()

    while line:
        lines.append(line)
        line = f.readline()

    return lines

def getDiffBy1(lines):
    for line1 in lines:
        for line2 in lines:
            matchedCharacters = []
            diffCount = 0

            if len(line1) == len(line2):
                for i in range(len(line1)):
                    c1 = line1[i]
                    c2 = line2[i]

                    if c1 != c2:
                        diffCount += 1
                    else:
                        matchedCharacters.append(c1)

            if diffCount == 1:
                return matchedCharacters

with open(filename) as f:
    lines = getLines(f)
    diffBy1 = getDiffBy1(lines)

    print "".join(str(x) for x in diffBy1).strip()

