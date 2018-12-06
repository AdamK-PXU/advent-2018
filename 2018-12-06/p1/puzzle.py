import sys

filename = "input.txt"

class Counter(dict):
    def __missing__(self, key):
        return 0

with open(filename) as f:
    counter = Counter()
    xMin = sys.maxsize
    xMax = -sys.maxsize
    yMin = sys.maxsize
    yMax = -sys.maxsize

    coordinates = []

    line = f.readline().strip()

    while line:
        coordinate = line.split(',')
        coordinate = (int(coordinate[0]), int(coordinate[1]))
        coordinates.append(coordinate)

        if coordinate[0] < xMin:
            xMin = coordinate[0]

        if coordinate[0] > xMax:
            xMax = coordinate[0]

        if coordinate[1] < yMin:
            yMin = coordinate[1]

        if coordinate[1] > yMax:
            yMax = coordinate[1]

        line = f.readline().strip()

    area = [[[(False, False), sys.maxsize] for x in range(xMax - xMin)] for y in range(yMax - yMin)]

    for coordinate in coordinates:
        for i in range(len(area)):
            for j in range(len(area[i])):
                distance = abs(coordinate[0] - (i + xMin)) + abs(coordinate[1] - (j + yMin))

                if distance < area[i][j][1]:
                    area[i][j] = [coordinate, distance]
                elif distance == area[i][j][1]:
                    area[i][j] = [(False, False), distance]

    for i in range(len(area)):
        for j in range(len(area[i])):
            coordinate = area[i][j][0]

            if coordinate != (False, False):
                if counter[coordinate] == -1:
                    continue
                else:
                    if i == 0 or i == len(area) - 1:
                        counter[coordinate] = -1
                    elif j == 0 or j == len(area[i]) - 1:
                        counter[coordinate] = -1
                    else:
                        counter[coordinate] += 1

    largestArea = 0

    for key, value in counter.items():
        if value > largestArea:
            largestArea = value

    print largestArea
