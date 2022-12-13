PART = 2 # 1 or 2

from operator import mul, add
import functools

class equation:
    def __init__(this, instr) -> None:
        parts = instr.split()
        this.old =   0
        this.a =     "old" if parts[0] == "old" else int(parts[0])
        this.func =  mul if parts[1] == "*" else add
        this.b =     "old" if parts[2] == "old" else int(parts[2])
        this.instr = instr

    def getInfo(this, mod):
        this.old = 1
        return this.instr + f" ({'old('+str(this.old)+')' if this.a == 'old' else this.a} * {'old('+str(this.old)+')' if this.b == 'old' else this.b} = {this.__call__(1, mod)})"

    def __call__(this, curVal, mod = 0) -> int:
        this.old = curVal if PART == 1 else curVal % mod
        return this.func(
            this.old if this.a == "old" else this.a,
            this.old if this.b == "old" else this.b
        )

def getThrowToFunc(test, iftrue, iffalse):
    #if PART == 1:
    return lambda curVal:iftrue if curVal%test==0 else iffalse
    #else:
    #    return lambda x:x==0

class monkey:
    def __init__(this, init: str) -> None:
        this.lines = init.split("\n")
        this.items = list(map(int, this.lines[1][18:].split(", ")))
        this.equation = equation(this.lines[2][19:])
        this.checkThrowTo = getThrowToFunc(
            int(this.lines[3][21:]),
            int(this.lines[4][29:]),
            int(this.lines[5][30:])
        )
        this.inspectCount = 0

    def disp(this, mod):
        print(this.items)
        print(this.equation.getInfo(mod))
        print(f"if worry divisible by {this.lines[3][21:]} toss to {this.lines[4][29:]} else {this.lines[5][30:]}")
        print(f"Inspected {this.inspectCount} items")
        print()

    def runTurn(this, monkeys, mod = 0):
        for i in this.items:
            this.inspectCount += 1
            new = 0
            if PART == 1:
                new = this.equation(i)//3
            else:
                new = this.equation(i, mod)
            monkeys[this.checkThrowTo(new)].items.append(new)
        this.items = []

with open("11.txt","r") as f:
    monkeyTexts = f.read().split("\n\n")
    monkeys = []
    mod = 0

    for i in monkeyTexts:
        monkeys.append(monkey(i))

    if PART == 2:
        mod = functools.reduce(lambda x,y:x*y, map(lambda x:int(x.lines[3][21:]), monkeys))

    for i in range(20 if PART == 1 else 10000):
        for m in monkeys:
            m.runTurn(monkeys, mod)

    print(list(map(
        lambda x:x.disp(mod),
        monkeys
    )))
    print(list(map(lambda x:x.inspectCount,monkeys)))
    print(list(sorted(map(lambda x:x.inspectCount,monkeys))))
    print(mul(*(list(sorted(map(lambda x:x.inspectCount,monkeys)))[-2:])))
