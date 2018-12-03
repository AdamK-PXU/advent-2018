import re

filename = "input.txt"

with open(filename) as f:
    regex = re.compile("#([0-9]+) @ ([0-9]{1,4}),([0-9]{1,4}): ([0-9]{1,4})x([0-9]{1,4})")
    overlapCount = 0
    fabric = [[0 for x in range(1000)] for y in range(1000)]

    line = f.readline()

    while line:
        matches = re.search(regex, line)
        x = int(matches.group(2))
        y = int(matches.group(3))
        width = int(matches.group(4))
        height = int(matches.group(5))

        for i in range(width):
            for j in range(height):
                fabric[x + i][y + j] += 1

                if fabric[x + i][y + j] == 2:
                    overlapCount += 1

        line = f.readline()

    print overlapCount
