################################################################################################
## Packages
################################################################################################

from numpy import loadtxt

################################################################################################
## Prepare input
################################################################################################

                                                ################################################
                                                ## Read in file(s)
                                                ################################################

inputFile = "AoC_2022Dec02_input.txt"
exampleFile = "AoC_2022Dec02_example.txt"

#with open(inputFile) as d:
with open(exampleFile) as d:
    data_raw = [line.strip("\n") for line in d.readlines()]
    # strategy guide

                                                ################################################
                                                ## Process raw into cleaned lis of lists of ints
                                                ################################################

#print(data_raw)

data_clean = []

for entry in data_raw:
    data_clean.append(entry.split(' '))

#print(data_clean)

opponent_key = {"A": "Rock", "B": "Paper", "C": "Scissors"}
your_key = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

points_key = {"Rock": 1, "Paper": 2, "Scissors": 3}

results_key = {"Win": 6, "Draw": 3, "Lose": 0}

################################################################################################
## Part 1 solution
################################################################################################

def youWin(opponents_throw, your_throw):
    if (opponents_throw == "Rock" and your_throw == "Paper") or (opponents_throw == "Paper" and your_throw == "Scissors") or (opponents_throw == "Scissors" and your_throw == "Rock"):
        return True

    else:
        return False

def playRPS(strategy):
    # accepts strategy list e.g. (['A', 'Y'])

    opponents_throw = opponent_key[strategy[0]]
    your_throw = your_key[strategy[1]]

    #print(opponents_throw, your_throw)

    points = points_key[your_throw]

    if youWin(opponents_throw, your_throw):
        #result = "Win"
        points += 6
    if youWin(your_throw, opponents_throw):
        #result = "Lose"
        points += 0
    if opponents_throw == your_throw:
        #result = "Draw"
        points += 3

    #points += results_key[result]

    return points

total_score = 0

for entry in data_clean:
    total_score += playRPS(entry)
    #print(playRPS(entry))

print(f"\nTotal score: {total_score}")

################################################################################################
## Part 2 solution
################################################################################################

