with open('inputs/day7.txt') as inputt:
  source = inputt.readlines()
class TreeNode:
  def __init__(self, data, prev):
    self.data = data
    self.prev = prev
    self.children1 = []
    self.children2 = []
    self.children3 = []
    self.children4 = []
    self.children5 = []
    self.children6 = []
    self.children7 = []
    self.children8 = []
    self.children9 = []
    self.children10 = []
    self.size = 0



totalsize = 0
for index, line in enumerate(source):


  lines = line.strip()
  linie = lines.split()
  if linie[0] == "$" and linie[1] == "cd":
    if linie[2] == "..":
      # TODO Code für Verzeichniss zurück einfügen
      print("yes")
      exec("currdir = " + currdir + ".prev")
      exec("prevdir = " + currdir + ".prev")
      if not len(sizeprevdir) == 0:
        exec("sizecurrdir = " + sizecurrdir + ".prev")
        exec("sizeprevdir = " + sizecurrdir + ".prev")
    elif linie[2] == "/":
      prevdir = ""
      currdir = "Root"
      sizeprevdir = ""
      sizecurrdir = "Root"

    else:
      # TODO Code für Verzeichniss weiter einfügen
      prevdir = currdir
      currdir = linie[2]
      sizeprevdir = sizecurrdir
      sizecurrdir = linie[2]


  elif linie[0] == "$" and linie[1] == "ls":
    nex = 1

    linebefor = source[int(index) - int(nex)]
    linesbefor = linebefor.strip()
    liniebefor = linesbefor.split()

    nextline = source[int(index) + int(nex)]
    nextlines = nextline.strip()
    nextlinie = nextlines.split()

    directory = []
    while nextlinie[0] != "$":
      print(nextlinie)
      directory.append(nextlines)
      nex += 1
      if int(index) + int(nex) >= len(source):
        exec(currdir + " = TreeNode(directory, prevdir)")
        leng = 0
        leng1 = 1
        exec("lengdata = len(" + currdir + ".data)")
        while leng < lengdata:
          exec("dataleng = " + currdir + ".data[leng]")
          exec("currchild = " + currdir + ".data[leng].split()[0]")
          if currchild == 'dir':
            exec(currdir + ".children" + str(leng1) + " = " + "'" + dataleng + "'")
            leng1 += 1
          elif not currchild == 'dir':
            fsize = int(currchild)
            exec(currdir + ".size += fsize")
          leng += 1
        exec("print(" + currdir + ".size)")
        exec("currdirsize = " + currdir + ".size")
        print(currdir)
        if int(currdirsize) <= 100000 and not totalsize >= 100000 and not int(currdirsize) + totalsize > 100000:
          totalsize += currdirsize
        elif int(currdirsize) + totalsize > 100000:
          total = "Total"
          print(totalsize)
          print(total)
          raise SystemExit
      nextline = source[int(index) + int(nex)]
      nextlines = nextline.strip()
      nextlinie = nextlines.split()
    if currdir == "Root":
      Root = TreeNode(directory, prevdir)
      leng = 0
      leng1 = 1
      while leng < len(Root.data):
        if Root.data[leng].split()[0] == "dir":
          exec("Root.children" + str(leng1) + " = Root.data[leng]")
          leng1 += 1
        elif not Root.data[leng].split()[0] == "dir":
          fsize = int(Root.data[leng].split()[0])
          Root.size += fsize
        leng += 1
      exec("print(" + currdir + ".size)")
      print(currdir)
    elif not currdir == "Root":
      exec(currdir + " = TreeNode(directory, prevdir)")
      leng = 0
      leng1 = 1
      exec("lengdata = len(" + currdir + ".data)")
      while leng < lengdata:
        exec("dataleng = " + currdir + ".data[leng]")
        exec("currchild = " + currdir + ".data[leng].split()[0]")
        if currchild == 'dir':
          exec(currdir + ".children" + str(leng1) + " = " + "'" + dataleng + "'")
          leng1 += 1
        elif not currchild == 'dir':
          fsize = int(currchild)
          exec(currdir + ".size += fsize")
        leng += 1
      exec("print(" + currdir + ".size)")
      exec("currdirsize = " + currdir + ".size")
      print(currdir)
      exec("datacurrdir = [item.split()[0] for item in " + currdir + ".data]")
      while not len(sizeprevdir) == 0:
        exec(sizeprevdir + ".size += " + currdir + ".size")
        exec("sizecurrdir = " + sizecurrdir + ".prev")
        exec("sizeprevdir = " + sizecurrdir + ".prev")
      if int(currdirsize) <= 100000 and not totalsize >= 100000 and not int(currdirsize) + totalsize > 100000:
        totalsize += currdirsize
        print("yes")
      elif int(currdirsize) + totalsize > 100000 and not int(currdir) > 100000:
        total = "Total"
        print(totalsize)
        print(total)
        raise SystemExit
