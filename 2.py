table = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    "X": 1,  # Rock,     Lose
    "Y": 2,  # Paper,    Tie
    "Z": 3  # Scissors, Win
}

smartMovePicker = {
    1: {1: 3, 2: 1, 3: 2},
    2: {1: 1, 2: 2, 3: 3},
    3: {1: 2, 2: 3, 3: 1}
}


def scoreRound(a, b):
    score = b
    if a == b:
        score += 3
    elif b - a in [1, -2]:
        score += 6
    return score


def smartScoreRound(a, b):
    b = smartMovePicker[b][a]
    return scoreRound(a, b)


with open("2.txt", "r") as f:
    rounds = f.readlines()
    score = 0
    smartscore = 0

    for round in rounds:
        a, b = round.split(" ")
        score += scoreRound(table[a.strip()], table[b.strip()])
        smartscore += smartScoreRound(table[a.strip()], table[b.strip()])

    print("Naive score:", score)
    print("Smart score:", smartscore)
