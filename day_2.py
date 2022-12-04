score = [
    [3, 0, 6],
    [6, 3, 0],
    [0, 6, 3]
]
shape = [1,2,3]
map_1 = {"A": 0, "B": 1, "C": 2}
map_2 = {"X": 0, "Y": 1, "Z": 2}

def convert(item):
    return (map_1[item[0]], map_2[item[1]])

with open("./day_2_input.txt", "r") as file: 
    data = [convert(x.strip('\n').split()) for x in file.readlines()]
    ans = 0
    for x, y in data:
        ans += score[y][x] + shape[y]
    print(ans)
    # for i in range(1, len(data)):
    #     if data[i]:
    #         data[i] += data[i-1]
    # print(max(data))
    # data.sort(reverse=True)
    # print(sum(data[:3]))