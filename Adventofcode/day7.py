with open('inputs/day7.txt') as f:
    source = f.readlines()

for index, line in enumerate(source):
    lines = line.strip()
    linie = lines.split()
    if linie[0] == "$" and linie[1] == "cd":
        if linie[2] == "..":
            # TODO Code für Verzeichniss zurück einfügen
            continue
        elif linie[2] == "/":
            continue
        else:
            # TODO Code für Verzeichniss weiter einfügen
            currdir = linie[2]
            exec(currdir + " = []")
    elif linie[0] == "$" and linie[1] == "ls":
        nex = 1

        linebefor = source[int(index) - int(nex)]
        linesbefor = linebefor.strip()
        liniebefor = linesbefor.split()

        nextline = source[int(index) + int(nex)]
        nextlines = nextline.strip()
        nextlinie = nextlines.split()

        while nextlinie[0] != "$":
            print(nextlinie)
            nex += 1
            if (int(index) + int(nex)) > len(source):
                exit()
            nextline = source[int(index) + int(nex)]
            nextlines = nextline.strip()
            nextlinie = nextlines.split()
