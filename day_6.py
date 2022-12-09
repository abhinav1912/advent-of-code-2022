with open("./day_6_input.txt", "r") as file:
    data = list([x.strip("\n") for x in file.readlines()][0])
    for i in range(13, len(data)):
        s = set(data[i-13:i+1])
        if len(s) == 14:
            print(i+1)
            break