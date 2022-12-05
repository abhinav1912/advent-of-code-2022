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
    ans = sum([value(intersection(x.strip('\n'))) for x in file.readlines()])
    print(ans)