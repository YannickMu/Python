with open('inputs/day6.txt') as f:
    source = f.readlines()

for line in source:
    SplitLine = []
    counter = 4
    lines = line.strip()
    for char in lines:
        SplitLine.append(str(char))
        if len(SplitLine) >= 4:
            if not SplitLine[-1] == SplitLine[-2] and not SplitLine[-1] == SplitLine[-3] and not SplitLine[-1] == SplitLine[-4] and not SplitLine[-1] == SplitLine[-2] and not SplitLine[-2] == SplitLine[-3] and not SplitLine[-2] == SplitLine[-4] and not SplitLine[-1] == SplitLine[-3] and not SplitLine[-2] == SplitLine[-3] and not SplitLine[-3] == SplitLine[-4]:
                print(counter)
                break
            else:
                counter += 1
