from numpy import loadtxt

with open("day2_input.txt") as d:
    data = [line.strip('\n') for line in d.readlines()]

#part 1
sub_position = {'hor_pos':0 , 'depth':0}


def move_sub(command):
    if command[:-2] == 'forward':
        sub_position['hor_pos'] += int(command[-1])
    if command[:-2] == 'down':
        sub_position['depth'] += int(command[-1])
    if command[:-2] == 'up':
        sub_position['depth'] -= int(command[-1])
        
def follow_route(directions):
    for dirs in directions:
        move_sub(dirs)


follow_route(data)

print(f"The product of final horizontal position and depth is {sub_position['hor_pos']*sub_position['depth']}.")


#part 2

sub_position2 = {'hor_pos':0 , 'depth':0 , 'aim':0}


def move_sub2(command):
    if command[:-2] == 'forward':
        sub_position2['hor_pos'] += int(command[-1])
        sub_position2['depth'] += sub_position2['aim']*int(command[-1])
    if command[:-2] == 'down':
        sub_position2['aim'] += int(command[-1])
    if command[:-2] == 'up':
        sub_position2['aim'] -= int(command[-1])

def follow_route2(directions):
    for dirs in directions:
        move_sub2(dirs)


follow_route2(data)

print(f"The product of final horizontal position and depth with modified commands is {sub_position2['hor_pos']*sub_position2['depth']}.")
     
