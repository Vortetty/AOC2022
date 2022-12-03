SOLVE_PART = 1 # 1 or 2

#
# Instead of set intersection i manually do an intersection then exit immediately after i find the first one
# The set intersection has massively high complexity (conversion is O(n) at best, then you have O(n*n + n) for intersecting)
# My method it at worst O(n*n + n), and could be significantly shortened depending on the positions of the shared character
#

def getPri(a):
    a = ord(a)
    if   a > 0x60: return a - 0x60
    elif a > 0x40: return a - 0x26

with open("3.txt", "r") as f:
    if SOLVE_PART == 1:
        bags = map(lambda x:[x[:len(x)//2], x[len(x)//2:]], f.readlines())
        total = 0
        for bag in bags:
            for a in bag[0]:
                if a in bag[1]:
                    total += getPri(a)
                    break
        print(total)
    elif SOLVE_PART == 2:
        bags = list(map(str.strip, f.readlines()))
        total = 0
        for bagnum in range(0, len(bags), 3):
            bag1 = bags[bagnum]
            bag2 = bags[bagnum+1]
            bag3 = bags[bagnum+2]
            for a in bag1:
                if a in bag2 and a in bag3:
                    total += getPri(a)
                    break
        print(total)