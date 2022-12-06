ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'
DRAW = 'DRAW'
WIN = 'WIN'
LOSE = 'LOSE'

encryption = {'A': ROCK, 'B': PAPER, 'C': SCISSORS,
           'X': LOSE, 'Y': DRAW, 'Z': WIN}

def move(they, strategy):
    if strategy == DRAW:
        return they
    
    winLose = {(ROCK, LOSE): SCISSORS, (ROCK, WIN): PAPER,
               (PAPER, LOSE): ROCK, (PAPER, WIN): SCISSORS,
               (SCISSORS, LOSE): PAPER, (SCISSORS, WIN): ROCK}
    return winLose[(they, strategy)]

def outcomeScore(they, me):
    if they == me:
        return 3
    elif they == ROCK and me == PAPER:
        return 6
    elif they == PAPER and me == SCISSORS:
        return 6
    elif they == SCISSORS and me == ROCK:
        return 6
    else:
        return 0

choiceScore = {ROCK: 1, PAPER: 2, SCISSORS: 3}

input = []
with open('2/input.txt') as f:
    rounds = f.readlines()

score = 0

for round in rounds:
    they = encryption[round[0]]
    strategy = encryption[round[2]]
    me = move(they, strategy)
    score += outcomeScore(they, me) + choiceScore[me]

print(score)