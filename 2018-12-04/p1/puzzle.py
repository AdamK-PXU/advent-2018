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
                    counter[currentGuardId][0] += awakeAsleepTime - currentSleepStartTime

                    for i in range(awakeAsleepTime - currentSleepStartTime):
                        counter[currentGuardId][1][i + currentSleepStartTime] += 1
                else:
                    counter[currentGuardId] = [0, [0 for i in range(60)]]

    longestSleepDurationId = 0
    longestSleepDuration = 0
    longestSleepMinutes = []

    for key, value in counter.items():
        if value[0] > longestSleepDuration:
            longestSleepDurationId = key
            longestSleepDuration = value[0]
            longestSleepMinutes = value[1]

    frequentlyAsleepOnMinute = 0
    frequentlyAsleepOnMinuteCount = 0

    for i in range(len(longestSleepMinutes)):
        minute = longestSleepMinutes[i]
        if minute > frequentlyAsleepOnMinuteCount:
            frequentlyAsleepOnMinute = i
            frequentlyAsleepOnMinuteCount = minute

    print (int(longestSleepDurationId) * int(frequentlyAsleepOnMinute))
