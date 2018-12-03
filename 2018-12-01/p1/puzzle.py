import string

filename = "input.txt"

with open(filename) as f:
    frequency = 0
    line = f.readline()

    while line:
        frequency += int(line)
        line = f.readline()

    print frequency

