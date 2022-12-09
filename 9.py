# all vars named "*pos" are just [x, y]
from math import dist as getDist

def getSurroundings(pos):
    x, y = pos
    return {
        (x+1, y),
        (x+1, y+1),
        (x,   y+1),
        (x-1, y+1),
        (x-1, y),
        (x-1, y-1),
        (x,   y-1),
        (x+1, y-1)
    }

def calcTailPos(headPos, tailPos):
    if getDist(headPos, tailPos) >= 2:
        return min(getSurroundings(headPos) & getSurroundings(tailPos), key=lambda x:getDist(x, headPos))
    else:
        return tailPos

dirFuncs = {
    "U": lambda x:[x[0], x[1]+1],
    "D": lambda x:[x[0], x[1]-1],
    "L": lambda x:[x[0]-1, x[1]],
    "R": lambda x:[x[0]+1, x[1]]
}

with open("9.txt","r") as f:
    visited1 = set()
    visited2 = set()
    head = [0, 0]
    TAIL_COUNT = 9
    tails = [[0, 0] for i in range(TAIL_COUNT)]
    for line in map(str.strip, f.readlines()):
        if len(line) > 0:
            direction, times = line.split()
            dirFunc = dirFuncs[direction]
            for i in range(int(times)):
                head = dirFunc(head)
                tails[0] = calcTailPos(head, tails[0])
                for i in range(1, len(tails)):
                    tails[i] = calcTailPos(tails[i-1], tails[i])
                visited1.add(",".join(map(str, tails[0])))
                visited2.add(",".join(map(str, tails[-1])))
    print("PT 1.", len(visited1))
    print("PT 2.", len(visited2))