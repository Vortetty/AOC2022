SOLVE_PART = 1 # 1 or 2

with open("4.txt", "r") as f:
    if SOLVE_PART == 1:
        isectElves = 0
        for line in f.readlines():
            e1, e2 = list(map(list, map(lambda x:map(int,x), map(lambda x:x.strip().split("-"), line.split(",")))))
            if (e1[0] <= e2[0] and e1[1] >= e2[1] or e2[0] <= e1[0] and e2[1] >= e1[1]): isectElves += 1
        print(isectElves)

    elif SOLVE_PART == 2:
        isectElves = 0
        for line in f.readlines():
            e1, e2 = list(map(list, map(lambda x:map(int,x), map(lambda x:x.strip().split("-"), line.split(",")))))
            if (e2[0] >= e1[0] and e2[0] <= e1[1] or e1[0] >= e2[0] and e1[0] <= e2[1]): isectElves += 1
        print(isectElves)