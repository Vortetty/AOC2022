SOLVE_PART = 1 # 1 or 2

def tryInt(x):
    try:
        return int(x)
    except:
        return

with open("5.txt", "r") as f:
    crates = []
    curLine = ""
    while (curLine := f.readline()) != "\n":
        crates.append(curLine)
    crates = list(map(lambda x:list(filter(lambda x:not x.startswith(" "), x[1:])), filter(lambda x:not (x[0].startswith(" ") or x[0].startswith("\n")), list(zip(*crates[::-1])))))

    if SOLVE_PART == 1:
        for line in map(lambda x:x.strip(), f.readlines()):
            if not line.startswith("move"): continue
            _, i1, _, i2, _, i3 = map(tryInt,line.split(" ")) # filter out garbage vars, i1 is the count to move, i2 is the source, i3 is the dest
            i3 -= 1
            i2 -= 1
            crates[i3] += crates[i2][-i1:][::-1]
            crates[i2] = crates[i2][:-i1]
    elif SOLVE_PART == 2:
        for line in map(lambda x:x.strip(), f.readlines()):
            if not line.startswith("move"): continue
            _, i1, _, i2, _, i3 = map(tryInt,line.split(" ")) # filter out garbage vars, i1 is the count to move, i2 is the source, i3 is the dest
            i3 -= 1
            i2 -= 1
            crates[i3] += crates[i2][-i1:]
            crates[i2] = crates[i2][:-i1]

    print("".join(map(lambda x:x[-1], crates)))
