import string

filename = "input.txt"

class Counter(dict):
    def __missing__(self, key):
        return 0

with open(filename) as f:
    twosCount = 0
    threesCount = 0
    line = f.readline()

    while line:
        twosLocal = 0
        threesLocal = 0
        counter = Counter()

        for c in line:
            counter[c] += 1

        for key, value in counter.items():
            if twosLocal == 0 and value == 2:
                twosLocal += 1
                twosCount += 1
            elif threesLocal == 0 and value == 3:
                threesLocal += 1
                threesCount += 1

        line = f.readline()

    print twosCount * threesCount

