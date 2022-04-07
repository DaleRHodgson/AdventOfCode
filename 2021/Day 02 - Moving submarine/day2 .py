with open("day2_input.txt") as d:
    data = [line.strip('\n') for line in d.readlines()]

   
class Submarine:
    def __init__(self, _horizontal_position, _depth, _aim):
        self.horizontal_position = _horizontal_position
        self.depth = _depth
        self.aim = _aim

    def move(self, command):
        # applies move actions as instructions in Part 1
        instruction, amount = command.split(' ')
        if instruction == 'forward':
            self.horizontal_position += int(amount)
            self.depth += self.aim*int(amount)
        if instruction == 'down':
            self.depth += int(amount)
        if instruction == 'up':
            self.depth -= int(amount)

    def move2(self,command):
        # applies move actions as instructions in Part 2 
        instruction, amount = command.split(' ')
        if instruction == 'forward':
            self.horizontal_position += int(amount)
            self.depth += self.aim*int(amount)
        if instruction == 'down':
            self.aim += int(amount)
        if instruction == 'up':
            self.aim -= int(amount)


#### Part 1
# initialise submarine and follow instructions with part 1 move method 

HMSdale = Submarine(0,0,0)
for dirs in data:
    HMSdale.move(dirs)

print(f"The product of final horizontal position and depth is {HMSdale.horizontal_position*HMSdale.depth}.")


#### Part 2
# initialise submarine and follow instructions with part 2 method

HMSdale2 = Submarine(0,0,0)
for dirs in data:
    HMSdale2.move2(dirs)

print(f"The product of final horizontal position and depth with modified commands is {HMSdale2.horizontal_position*HMSdale2.depth}.")
