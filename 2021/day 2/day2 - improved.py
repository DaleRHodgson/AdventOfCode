with open("day2_input.txt") as d:
    data = [line.strip('\n') for line in d.readlines()]

   
class Submarine:
    def __init__(self, _horizontal_position, _depth, _aim):
        self.horizontal_position = _horizontal_position
        self.depth = _depth
        self.aim = _aim

    def move(self,command):
        instruction, amount = command.split(' ')
        if instruction == 'forward':
            self.horizontal_position += int(amount)
            self.depth += self.aim*int(amount)
        if instruction == 'down':
            self.aim += int(amount)
        if instruction == 'up':
            self.aim -= int(amount)

HMSdale = Submarine(0,0,0)

for dirs in data:
    HMSdale.move(dirs)

print(f"The product of final horizontal position and depth with modified commands is {HMSdale.horizontal_position*HMSdale.depth}.")
