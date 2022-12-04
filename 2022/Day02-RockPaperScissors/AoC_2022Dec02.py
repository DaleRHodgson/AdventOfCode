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

with open(inputFile) as d:
#with open(exampleFile) as d:
    data_raw = [line.strip("\n") for line in d.readlines()]
    # strategy list

                                                ################################################
                                                ## Process raw into cleaned lis of lists of ints
                                                ################################################

data_clean = []

for entry in data_raw:
    data_clean.append(entry.split(' '))

opponent_key = {"A": "Rock", "B": "Paper", "C": "Scissors"}
your_key = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

points_key = {"Rock": 1, "Paper": 2, "Scissors": 3}

# table[opponents_throw][you_throw]
table = {"Rock": {"Rock": "Draw", "Paper": "Win", "Scissors": "Lose"},
         "Paper": {"Rock": "Lose", "Paper": "Draw", "Scissors": "Win"},
         "Scissors": {"Rock": "Win", "Paper": "Lose", "Scissors": "Draw"}
        }

results_key = {"Win": 6, "Draw": 3, "Lose": 0}

def get_score(opponents_throw, your_throw):
    res = table[opponents_throw][your_throw]
    
    return results_key[res]

################################################################################################
## Part 1 solution
################################################################################################

def playRPS(strategy):
    # accepts strategy list e.g. (['A', 'Y'])

    opponents_throw = opponent_key[strategy[0]]
    your_throw = your_key[strategy[1]]

    points = points_key[your_throw] + get_score(opponents_throw, your_throw)

    return points

total_score = 0

for entry in data_clean:
    total_score += playRPS(entry)

print(f"#### Part 1\nTotal score: {total_score}\n")

################################################################################################
## Part 2 solution
################################################################################################

outcome_key = {"X": "Lose", "Y": "Draw", "Z": "Win"}

def playRPS2(strategy):

    opponents_throw = opponent_key[strategy[0]]
    desired_outcome = outcome_key[strategy[1]]

    your_throw_index = list(table[opponents_throw].values()).index(desired_outcome)
    your_throw = list(table[opponents_throw].keys())[your_throw_index]

    points = points_key[your_throw] + results_key[desired_outcome]

    return points

total_score = 0

for entry in data_clean:
    total_score += playRPS2(entry)

print(f"#### Part 2\nTotal score: {total_score}\n")
