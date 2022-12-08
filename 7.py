import json

with open("7.txt","r") as f:
    dirStack = []
    files = {
        "//": [0, 0]
    }

    # files will follow the format `size`
    # folders will follow `{ files }`
    line = f.readline()
    while line:
        print(line, end="")
        if line.startswith("$ cd"):
            print("changedir", dirStack)
            dirStack.append(line[5:-1]) if line.find("..") == -1 else dirStack.pop()
            line = f.readline()
        elif line.startswith("$ ls"):
            while not (line := f.readline()).startswith("$") and line:
                print(line, end="")
                if line.startswith("dir "):
                    files["/".join(dirStack) + "/" + line[4:-1]] = [0, 0]
                elif line.split()[0].isnumeric():
                    size = int(line.split()[0])
                    files["/".join(dirStack) + "/" + line.split(" ")[1][:-1]] = [1, size]

                    toCascade = []
                    tmp = []
                    for i in dirStack:
                        toCascade.append("/".join(tmp) + "/" + i)
                        tmp.append(i)

                    #print(toCascade)

                    keys = files.keys()
                    for name in toCascade:
                        if name in keys:
                            if files[name][0] == 0:
                                files[name][1] += size
        print("")

    #print(json.dumps(files, indent=4))
    #print(json.dumps(list(map(lambda x:f"{x[0]} {x[1][1]}", filter(lambda x:x[1][0]==0, files.items()))), indent=4))

    dirs = list(map(lambda x:x[1], list(filter(lambda x:x[1][0]==0 and x[0]!="//", files.items()))))
    usedUnderVal = sum(map(lambda x:x[1], filter(lambda x:x[1]<10**5, dirs)))
    print("PT 1. >>", usedUnderVal)

    total     = 70000000
    needed    = 30000000
    used      = files["//"][1]
    free      = total-used
    minDelete = needed-free

    dirToDelete = min(filter(lambda x:x[1]>=minDelete, dirs), key=lambda x:x[1])
    print("PT 2. >>", dirToDelete[1])
