def check(x, y):
    return ((int(x[0]) >= int(y[0])) and (int(x[1]) <= int(y[1])))
def intersect(s):
    x,y = [int(i) for i in s[0].split("-")], [int(i) for i in s[1].split("-")]
    return (overlap(x,y))

def temp(x,y):
    return (x >= y[0]) and (x <= y[1])

def overlap(x,y):
    return (
        temp(x[0], y) or
        temp(x[1], y) or
        temp(y[0], x) or
        temp(y[1], x)
    )

with open("./day_4_input.txt", "r") as file:
    data = sum([int(intersect(x.strip("\n").split(","))) for x in file.readlines()])
    print(data)