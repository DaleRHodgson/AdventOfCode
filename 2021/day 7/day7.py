from math import floor, ceil

with open("day7_input.txt") as d:
    data = [ int(entry) for entry in d.readline().strip('\n').split(',') ]
    data.sort()

test_data = [16,1,2,0,4,2,7,1,2,14]
test_data.sort()

#part 1
def get_median(positions):
    return(positions[len(positions)//2])

key_pos1 = get_median(data)

part1_fuel = sum([abs(pos-key_pos1) for pos in data])

print(f"part 1 sum = {part1_fuel}" )
    

# part 2
def get_mean(positions):
    return(sum(positions)/len(positions))

#key pos between mean-0.5 and mean+0.5
key_pos2a = floor(get_mean(data))
key_pos2b = ceil(get_mean(data))

def fuel_cost(start_pos, end_pos):
    return( int(((start_pos-end_pos)**2 + abs(start_pos-end_pos))/2 ))

part2_fuela = sum( [ fuel_cost(pos,key_pos2a) for pos in data ] )
part2_fuelb = sum( [ fuel_cost(pos,key_pos2b) for pos in data ] )

print(f"part 2 sum = {min(part2_fuela,part2_fuelb)}")
