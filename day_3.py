def intersection(s):
    s1, s2 = set(s[:len(s)//2]), set(s[len(s)//2:])
    for i in s1:
        if i in s2:
            return i

def value(s):
    if s >= "a" and s <= "z":
        return ord(s) - ord("a") + 1
    return ord(s) - ord("A") + 27

with open("./day_3_input.txt", "r") as file:
    # ans = sum([value(intersection(x.strip('\n'))) for x in file.readlines()])
    data = [x.strip('\n') for x in file.readlines()]
    ans = 0
    for i in range(0, len(data), 3):
        x = set(data[i]) & set(data[i+1]) & set(data[i+2])
        for el in x:
            ans += value(el)
    print(ans)