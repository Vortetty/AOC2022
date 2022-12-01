with open("1.txt","r") as f:
    print([(elves:=list(map(lambda x:sum(map(int,filter(lambda y:len(y)>0, x.split("\n")))), f.read().split("\n\n")))), max(elves), sum(sorted(elves)[-3:])][-2:])
