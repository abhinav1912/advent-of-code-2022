def check(x, y):
    return ((int(x[0]) >= int(y[0])) and (int(x[1]) <= int(y[1])))
def intersect(s):
    x,y = [int(i) for i in s[0].split("-")], [int(i) for i in s[1].split("-")]
    # print(x,y)
    return (check(x,y) or check(y,x))

with open("./day_4_input.txt", "r") as file:
    data = sum([int(intersect(x.strip("\n").split(","))) for x in file.readlines()])
    print(data)