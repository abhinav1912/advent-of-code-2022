with open("./day_1_input.txt", "r") as file:
    data = [int(x.strip("\n")) if len(x)>2 else 0 for x in file.readlines()]
    for i in range(1, len(data)):
        if data[i]:
            data[i] += data[i-1]
    print(max(data))
    data.sort(reverse=True)
    print(sum(data[:3]))