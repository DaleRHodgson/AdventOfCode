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

inputFile = "AoC_2022Dec03_input.txt"
exampleFile = "AoC_2022Dec03_example.txt"

#with open(inputFile) as d:
with open(exampleFile) as d:
    data_raw = [line.strip("\n") for line in d.readlines()]
    # strategy list

                                                ################################################
                                                ## Process raw into cleaned lis of lists of ints
                                                ################################################

data_clean = []
#list of two element lists

for entry in data_raw:
    data_clean.append(entry.split(' '))

################################################################################################
## Part 1 solution
################################################################################################

def get_cuplicate(rucksacks):
    # accepts two element list

    duplicate = 'a'

    return duplicate

def get_priority(letter):

    return 1

priorities_sum = 0

for entry in data_clean:

    duplicate = get_duplicate(entry)

    priority = get_priority(duplicate)

    priorities_sum += priority

################################################################################################
## Part 2 solution
################################################################################################


