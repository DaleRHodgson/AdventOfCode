################################################################################################
## Packages
################################################################################################

from numpy import loadtxt, floor
import string

################################################################################################
## Prepare input
################################################################################################

                                                ################################################
                                                ## Read in file(s)
                                                ################################################

inputFile = "AoC_2022Dec03_input.txt"
exampleFile = "AoC_2022Dec03_example.txt"

with open(inputFile) as d:
#with open(exampleFile) as d:
    data_raw = [line.strip("\n") for line in d.readlines()]
    # rucksacks list

                                                ################################################
                                                ## Process raw into cleaned lis of lists of ints
                                                ################################################

data_clean = []
#list of two element lists

#print(data_raw)

for entry in data_raw:

    size = len(entry)
    midpoint = int(floor(size/2))
    
    data_clean.append([entry[:midpoint],entry[midpoint:]])

#print(data_clean)

################################################################################################
## Part 1 solution
################################################################################################

def get_duplicate(rucksack):
    # accepts two element list

    first_half = set(rucksack[0])
    second_half = set(rucksack[1])


    duplicate = first_half.intersection(second_half)

    return str(duplicate)[2]

def get_priority(letter):

    alphabet = string.ascii_lowercase + string.ascii_uppercase

    return alphabet.find(letter)+1

priorities_sum = 0

for entry in data_clean:

    duplicate = get_duplicate(entry)

    #print(duplicate)

    priority = get_priority(duplicate)

    #print(priority)

    priorities_sum += priority

print(f"#### Part 1\nSum of priorities = {priorities_sum}")

################################################################################################
## Part 2 solution
################################################################################################


