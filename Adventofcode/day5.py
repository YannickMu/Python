def run():
    with open('inputs/day5.txt') as f:
        source = f.readlines()
    if not source:
        raise ValueError("Es wurde kein Input gefunden!")
    stack = []
    anzahlspalten = 0
    for line in source:
        trimmedline = line.strip()
        if anzahlspalten == 0 and trimmedline[0] != "1":
            ebene = getebene(line)
            stack.append(ebene)
        elif anzahlspalten == 0:
            anzahlspalten = int(trimmedline[-1])
        elif not line.isspace():
            split = line.split()
            anzahl = int(split[1])

            while anzahl > 0:
                anzahl -= 1
                von = int(split[3]) - 1
                zu = int(split[5]) - 1

                topfromlevel = gettoplevel(stack, von)
                toptolevel = gettopemptylevel(stack, zu, anzahlspalten)
                toptolevel[zu] = topfromlevel[von]
                topfromlevel[von] = ""
    for i in range(len(stack)):
        for ii in range(anzahlspalten):
            if stack[i][ii] == "":
                stack[i][ii] = stack[i][ii].replace("", "   ")
        print(stack[i])


def getebene(line):
    start = 0
    end = 3
    result = []
    while end <= len(line):
        value = line[start:end]
        result.append(value.strip())
        start += 4
        end += 4
    return result


def gettoplevel(stack, spalte):
    level = 0
    while not stack[level][spalte]:
        level += 1

    return stack[level]


def gettopemptylevel(stack, spalte, anzahlspalten):
    level = 0
    while level < len(stack) and stack[level][spalte] == "":
        level += 1

    if level >= len(stack):
        return stack[-1]
    elif level > 0:
        return stack[level - 1]
    else:
        newebene = []
        for i in range(anzahlspalten):
            newebene.append("")
        stack.insert(0, newebene)
        return newebene


run()
