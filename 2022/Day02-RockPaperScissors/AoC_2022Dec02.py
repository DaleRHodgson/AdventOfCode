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

inputFile = "AoC_2022Dec01_input.txt"
exampleFile = "AoC_2022Dec01_example.txt"

with open(inputFile) as d:
#with open(exampleFile) as d:
    data_raw = [line.strip("\n") for line in d.readlines()]
    # list of calories carried by elves

                                                ################################################
                                                ## Process raw into cleaned lis of lists of ints
                                                ################################################

# make every sequence of entries terminate with ''
data_raw.append('')

# convert strings to int, replace '' with 0
data_ints = []
for val in data_raw:
    if val != '':
        data_ints.append(int(val))
    elif val == '':
        data_ints.append(0)

# identify seperation between entries
indexes_of_gaps = [0]
for index in range(len(data_ints)):
    if data_ints[index] == 0:
        indexes_of_gaps.append(index+1)

# create clean list of lists
input_clean = []
num_of_elves = len(indexes_of_gaps)

for i in range(num_of_elves-1):
    elf_start = indexes_of_gaps[i]
    elf_end = indexes_of_gaps[i+1]-1
    input_clean.append(data_ints[elf_start:elf_end])

################################################################################################
## Part 1 solution
################################################################################################

sums_of_cals = []
for elf in input_clean:
    sums_of_cals.append(sum(elf))

print("\n#### Part 1")
print(f"Elf {sums_of_cals.index(max(sums_of_cals))+1} is carrying the most calories with: {max(sums_of_cals)}")

################################################################################################
## Part 2 solution
################################################################################################

sums_of_cals.sort()
sum_top_three = sum(sums_of_cals[-3:])

print("\n#### Part 2")
print(f"The top three elves are carrying {sum_top_three} calories in total.")