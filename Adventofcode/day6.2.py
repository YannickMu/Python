with open('inputs/day6.txt') as f:
    source = f.readlines()

for line in source:
    SplitLine = []
    counter = 14
    lines = line.strip()
    for char in lines:
        dup = []
        SplitLine.append(str(char))
        if len(SplitLine) == 14:
            dup = [x for i, x in enumerate(SplitLine) if x in SplitLine[:i]]
            if not dup:
                print(counter)
                break
            else:
                counter += 1
                del(SplitLine[0])
