import re

dat = re.compile(r'\[(\w)\]')
com = re.compile(r'move (\d+) from (\d+) to (\d+)')
mem = [[] for i in range(9)]

file = open("./day_5_input.txt", "r")
for line in file.readlines():

    for match in re.finditer(dat, line):
            mem[match.start(1)//4].insert(0, match.group(1))
    op = re.findall(com, line)
    if op != []:
            op = op[0]
            mem[int(op[2])-1] += mem[int(op[1])-1][-int(op[0]):]
            mem[int(op[1])-1][-int(op[0]):] = []
            # for i in range(int(op[0])):
            #         mem[int(op[2])-1].append(mem[int(op[1])-1].pop())
                    

out = ""
for i in range(9):
    out += mem[i].pop()

print(out)