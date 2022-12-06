with open("6.txt", "r") as f:
    text = f.read()
    i = 3
    while (i := i+1):
        if len(set(text[i-4:i])) == 4: break
    print(f"PT.1 >> {i} ({text[i-4:i]})")

    i = 13
    while (i := i+1):
        if len(set(text[i-14:i])) == 14: break
    print(f"PT.2 >> {i} ({text[i-14:i]})")