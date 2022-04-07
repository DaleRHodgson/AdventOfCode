with open("day6_input.txt") as d:
    data = [ int(entry) for entry in d.readline().strip('\n').split(',') ]

test_data = [3,4,3,1,2]

#key = days until next spawn, value = number of fish of that age
fish_data = { 0:0,
              1:0,
              2:0,
              3:0,
              4:0,
              5:0,
              6:0,
              7:0,
              8:0
            }

#fill fish data
for fish in data:
    for age in fish_data.keys():
        if fish == age:
            fish_data[age] += 1

#### Part 1 / Part 2
# input is list of ints representing days until a given fish next spawn
# when a fish int reaches 0, that fish resets to state {6 days from spawning}
# and a new fish in state {8 days from spawning} is produced.
#
# Part 1: how many fish after 80 days?
# Part 2: how many fish after 255 days?

# Naive approach:
# Continue appending to the list new fish states.
# An exponential workload which is infeasible for part 2
def iter_day(fish_states):
    #countdown all fish states
    for i in range(len(fish_states)):
        fish_states[i] -= 1
    #spawn
    for i in range(len(fish_states)):
        if fish_states[i] == -1:
            fish_states.append(8)
            fish_states[i] = 6
    return(fish_states)


# Robust approach:
# Only total number of fish is needed, so instead store
# a dict with the number of fish in each state,
# apply a linear operation per day.

# Method to step one day forward using fish_data
def iter_days():
    global fish_data
    fish_states = fish_data
    next_day = {    0:0,
                    1:0,
                    2:0,
                    3:0,
                    4:0,
                    5:0,
                    6:0,
                    7:0,
                    8:0
                }

    # fish that have just spawned reset to state {6 days from spawning}
    next_day[6] += fish_states[0]
    
    # number of fish in state n will be number of fish in
    # state n+1 on previous day
    # i.e. all fish not newly spawned tick down one day
    # state 0 wraps around to state 8 by module
    for age in range(9):
        next_day[age] += fish_states[(age+1)%9]
    
    fish_states = next_day
    fish_data = fish_states

# Iterate 255 days:
for i in range(256):
    iter_days()
    #print(f"day {i}: {sum(fish_data.values())}")
    if i == 79 or i == 255:
        print(f"Solution-\tday {i+1}: {sum(fish_data.values())}")

