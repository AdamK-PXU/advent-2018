import re
import time
import datetime

filename = "input.txt"

with open(filename) as f:
    counter = dict()
    regexId = re.compile("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:([0-9]{2})\][#a-zA-Z ]+([0-9]+)[a-zA-Z ]+")
    regexAwakeAsleep = re.compile("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:([0-9]{2})\] ([a-zA-Z ]+)")

    line = f.readline()
    lines = [];

    while line:
        lines.append(line)
        line = f.readline()

    lines = sorted(lines)

    currentGuardId = False
    currentSleepStartTime = False

    for line in lines:
        matchesId = re.search(regexId, line)
        matchesAwakeAsleep = re.search(regexAwakeAsleep, line)

        if matchesId:
            currentGuardId = matchesId.group(2)
        elif matchesAwakeAsleep:
            awakeAsleepTime = int(matchesAwakeAsleep.group(1))
            awakeAsleep = matchesAwakeAsleep.group(2)

            if awakeAsleep == 'falls asleep':
                currentSleepStartTime = awakeAsleepTime
            else:
                if currentGuardId in counter:
                    for i in range(awakeAsleepTime - currentSleepStartTime):
                        counter[currentGuardId][i + currentSleepStartTime] += 1
                else:
                    counter[currentGuardId] = [0 for i in range(60)]

    frequentlyAsleepMinutes = [[0, 0] for i in range(60)]

    for key, value in counter.items():
        for i in range(len(value)):
            if value[i] > frequentlyAsleepMinutes[i][1]:
                frequentlyAsleepMinutes[i][0] = key
                frequentlyAsleepMinutes[i][1] = value[i]

    mostFrequentlyAsleepMinuteId = 0
    mostFrequentlyAsleepMinuteCount = 0
    mostFrequentlyAsleepMinute = 0

    for i in range(len(frequentlyAsleepMinutes)):
        frequentlyAsleepMinute = frequentlyAsleepMinutes[i]

        if frequentlyAsleepMinute[1] > mostFrequentlyAsleepMinuteCount:
            mostFrequentlyAsleepMinuteId = frequentlyAsleepMinute[0]
            mostFrequentlyAsleepMinuteCount = frequentlyAsleepMinute[1]
            mostFrequentlyAsleepMinute = i

    print int(mostFrequentlyAsleepMinuteId) * int(mostFrequentlyAsleepMinute)
