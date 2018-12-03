import string

filename = "input.txt"

class Counter(dict):
    def __missing__(self, key):
        return 0

def duplicateFrequency(frequencyChanges):
    frequency = 0
    frequencyChangeIndex = 0
    counter = Counter()

    while counter[frequency] < 2:
        frequency += frequencyChanges[frequencyChangeIndex]
        counter[frequency] += 1
        frequencyChangeIndex += 1
        frequencyChangeIndex = frequencyChangeIndex % len(frequencyChanges)

    return frequency

with open(filename) as f:
    frequencyChanges = []
    line = f.readline()

    while line:
        frequencyChanges.append(int(line))
        line = f.readline()

    print duplicateFrequency(frequencyChanges)

