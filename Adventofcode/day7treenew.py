with open('inputs/day7.txt') as inputt:
  source = inputt.readlines()
  print(source)
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

    for index, line in enumerate(source):
        lines = line.strip()
        linesp = lines.split()

        if linesp[0] == "$" and linesp[1] == "cd":
            if linesp[2] == "/":
                curdir = "Root"
                prevdir = ""
            elif not linesp[2] == ".." and not prevdir == "":
                prevdir = curdir
                curdir = linesp[2]
            else:
                curdir = prevdir
                exec("prevdir = " + curdir + ".prev")
        elif linesp[0] == "$" and linesp[1] == "ls":
            print("ls")
            while not linesp[0] == "$":
                exec(curdir + ".size += int(linesp[0])")
                print(linesp)
