with open("day6_input.txt") as d:
    data = [ int(entry) for entry in d.readline().strip('\n').split(',') ]

test_data = [3,4,3,1,2]

def iter_day(fish_states):
    #countdown all fish ages
    for i in range(len(fish_states)):
        fish_states[i] -= 1
    #spawn
    for i in range(len(fish_states)):
        if fish_states[i] == -1:
            fish_states.append(8)
            fish_states[i] = 6
    return(fish_states)

#key = age, value=number of fish of that age
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

#function to step one day forward using fish_data
def iter_days():
    global fish_data
    fish_states = fish_data
    next_day = { 0:0,
              1:0,
              2:0,
              3:0,
              4:0,
              5:0,
              6:0,
              7:0,
              8:0
    }
    next_day[6] += fish_states[0]
    for age in range(9):
        next_day[age] = fish_states[(age+1)%9]
        next_day[6] += next_day[8]
    fish_states = next_day
    fish_data=fish_states

#part 1
##for i in range(80):
##    iter_days()
##    print(sum(fish_data.values()))

#part 2
for i in range(256):
    iter_days()
    print(sum(fish_data.values()))
