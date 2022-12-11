with open("10.txt","r") as f:
    clock = 1
    sigCount = 0
    regx = 1

    def drawPixel():
        if (clock-1) % 40 == 0:
            print()
        if clock % 5 == 1:
            print("  ", end="")
        print("#" if abs(regx-((clock-1)%40))<=1 else " ", end="")

    for line in map(lambda x:x.strip()[5:], filter(lambda x:x!="\n", f.readlines())):
        #print(f'"{line}"')
        if line == "":
            drawPixel()
            clock += 1
            if clock % 40 == 20:
                sigCount += regx * clock
        else:
            drawPixel()
            clock += 1
            if clock % 40 == 20:
                sigCount += regx * clock
            drawPixel()
            clock += 1
            regx += int(line)
            if clock % 40 == 20:
                sigCount += regx * clock
    print("\n" + str(sigCount))