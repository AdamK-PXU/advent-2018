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

    viableArea = 0

    for i in range(xMax - xMin):
        for j in range(yMax - yMin):
            distanceSum = 0

            for coordinate in coordinates:
                distanceSum += abs(coordinate[0] - (i + xMin)) + abs(coordinate[1] - (j + yMin))

            if distanceSum < 10000:
                viableArea += 1

    print viableArea
