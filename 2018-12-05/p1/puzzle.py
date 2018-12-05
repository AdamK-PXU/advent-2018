filename = "input.txt"

with open(filename) as f:
    polymer = f.readlines()
    polymer = polymer[0].strip()
    reducedPolymer = []

    for c in polymer:
        if len(reducedPolymer) > 0 and reducedPolymer[-1].upper() == c.upper():
            if reducedPolymer[-1].isupper() and c.isupper() != True:
                reducedPolymer.pop()
            elif reducedPolymer[-1].isupper() != True and c.isupper():
                reducedPolymer.pop()
            else:
                reducedPolymer.append(c)
        else:
            reducedPolymer.append(c)

    print len(reducedPolymer)
