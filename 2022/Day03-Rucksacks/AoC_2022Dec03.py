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
                                                ## Process raw into cleaned list
                                                ################################################

data_clean = []
#list of two element lists

for entry in data_raw:

    size = len(entry)
    midpoint = int(floor(size/2))
    
    data_clean.append([entry[:midpoint],entry[midpoint:]])

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

def get_shared_item(elves):
    #accepts three element list

    elf0 = set(elves[0])
    elf1 = set(elves[1])
    elf2 = set(elves[2])

    shared_item = elf0.intersection(elf1).intersection(elf2)

    return str(shared_item)[2]
    

priorities_sum = 0

for i in range(0,len(data_raw)-2,3):

    shared_item = get_shared_item([data_raw[i], data_raw[i+1], data_raw[i+2]])

    priorities_sum += get_priority(shared_item)

print(f"#### Part 2\nSum of priorities = {priorities_sum}\n")
