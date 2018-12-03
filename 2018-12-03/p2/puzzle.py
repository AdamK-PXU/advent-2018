import re

filename = "input.txt"

with open(filename) as f:
    regex = re.compile("#([0-9]+) @ ([0-9]{1,4}),([0-9]{1,4}): ([0-9]{1,4})x([0-9]{1,4})")
    overlapCount = 0
    fabric = [[[] for x in range(1000)] for y in range(1000)]
    claims = dict()

    line = f.readline()

    while line:
        matches = re.search(regex, line)
        claim = int(matches.group(1))
        x = int(matches.group(2))
        y = int(matches.group(3))
        width = int(matches.group(4))
        height = int(matches.group(5))

        claims[claim] = False

        for i in range(width):
            for j in range(height):
                fabric[x + i][y + j].append(claim)

                if len(fabric[x + i][y + j]) > 1:
                    for overlappingClaim in fabric[x + i][y + j]:
                        claims[overlappingClaim] = True

        line = f.readline()

    for key, value in claims.items():
        if not value:
            print key
