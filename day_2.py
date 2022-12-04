score = [
    [3, 0, 6],
    [6, 3, 0],
    [0, 6, 3]
]
shape = [1,2,3]
map_1 = {"A": 0, "B": 1, "C": 2}
map_2 = {"X": 0, "Y": 1, "Z": 2}
part_2_map = [0,3,6]

def convert(item):
    return (map_1[item[0]], map_2[item[1]])

def shape_for_score(x, y):
    for j in range(3):
        if score[j][x] == part_2_map[y]:
            return j

with open("./day_2_input.txt", "r") as file: 
    data = [convert(x.strip('\n').split()) for x in file.readlines()]
    ans = 0
    part_2 = 0
    for x, y in data:
        ans += score[y][x] + shape[y]
        part_2 += shape[shape_for_score(x, y)] + part_2_map[y]
    print(part_2)