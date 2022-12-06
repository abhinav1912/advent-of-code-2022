def check(x, y):
    return ((x[0] >= y[0]) and (x[1] <= y[1]))
def intersect(s):
    x,y = s[0].split("-"), s[1].split("-")
    return (check(x,y) or check(y,x))

with open("./day_4_input.txt", "r") as file:
    data = sum([int(intersect(x.strip("\n").split(","))) for x in file.readlines()])
    print(data)