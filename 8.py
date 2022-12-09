from colorsys import hsv_to_rgb
import math
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colorEase(x):
    return math.sqrt(1 - pow(x - 1, 2))


with open("8.txt","r") as f:
    grid = [
        [int(i) for i in line] for line in filter(str.__len__, map(str.strip, f.readlines()))
    ]
    tfgrid = []
    treeScores = []

    for i in range(len(grid)):
        tfgrid.append([])
        treeScores.append([])
        for j in range(len(grid[0])):
            tmp = j==0 or j == len(grid[0])-1 or i == 0 or i == len(grid)-1
            tfgrid[i].append(tmp)
            treeScores[i].append(int(tmp))

    #print(*map("".join, map(lambda x:map(str,x), grid)), sep="\n")

    widthIter  = range(1, len(grid[0])-1)      # Avoids testing edges, *tiny* time save but a time save nonetheless
    heightIter = range(1, len(grid)-1)         # Avoids testing edges, *tiny* time save but a time save nonetheless
    visible = len(grid)*2 + (len(grid[0])-2)*2 # All edges known visible
    print(f"{bcolors.ENDC}{visible}")
    print(f"{bcolors.ENDC}{len(list(heightIter)), len(list(widthIter))}")
    print(f"{bcolors.ENDC}{list(widthIter)}")
    print(f"{bcolors.ENDC}{list(heightIter)}")
    print()
    bestTreeVal = 0
    worstTreeVal = float('inf')
    for y in heightIter:
        tfgrid[y][0] = True
        tfgrid[y][-1] = True
        for x in widthIter:
            up = left = right = down = False # assume no trees are taller or equal
            ups = lefts = rights = downs = 0
            for i in range(y-1, -1, -1):
                ups += 1
                if grid[y][x] <= grid[i][x]:
                    up = True
                    break
            for i in range(y+1, len(grid)):
                downs += 1
                if grid[y][x] <= grid[i][x]:
                    down = True
                    break
            for i in range(x-1, -1, -1):
                lefts += 1
                if grid[y][x] <= grid[y][i]:
                    left = True
                    break
            for i in range(x+1, len(grid[0])):
                rights += 1
                if grid[y][x] <= grid[y][i]:
                    right = True
                    break
            if not all([up, down, left, right]):
                visible += 1
                tfgrid[y][x] = True
            treeScores[y][x] = ups*downs*lefts*rights
            bestTreeVal = max(treeScores[y][x], bestTreeVal)
            worstTreeVal = min(treeScores[y][x], worstTreeVal)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tmpColor = hsv_to_rgb(
                (120*colorEase((treeScores[i][j]-worstTreeVal)/(bestTreeVal-worstTreeVal)/2+.5) - 60*tfgrid[i][j])/360,
                1,
                max((colorEase((treeScores[i][j]-worstTreeVal)/(bestTreeVal-worstTreeVal))*.85 + .15) * 4, tfgrid[i][j])/4
            ) if bestTreeVal != treeScores[i][j] else (90/255, 200/255, 255/255)
            color = f"\033[38;2;{int(tmpColor[0]*255)};{int(tmpColor[1]*255)};{int(tmpColor[2]*255)}m"
            print(f"{color}{int(grid[i][j])}", end=bcolors.ENDC)
        print()
    print(f"{bcolors.ENDC}(green trees are hidden, yellow ones are visible, blue tree is the ideal tree, the brighter the color the closer it is to ideal)")
    print(f"Visible Trees:     {visible}")
    print(f"Best Tree's Score: {bestTreeVal}")
