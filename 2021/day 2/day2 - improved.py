with open("day2_input.txt") as d:
    data = [line.strip('\n') for line in d.readlines()]

   
class Submarine:
    def __init__(self, horizontal_position, depth, aim):
        self.horizontal_position = horizontal_position
        self.depth = depth
        self.aim = aim

    def move(self,command):
        if command[:-2] == 'forward':
            self.horizontal_position += int(command[-1])
            self.depth += self.aim*int(command[-1])
        if command[:-2] == 'down':
            self.aim += int(command[-1])
        if command[:-2] == 'up':
            self.aim -= int(command[-1])

HMSdale = Submarine(0,0,0)

for dirs in data:
    HMSdale.move(dirs)

print(f"The product of final horizontal position and depth with modified commands is {HMSdale.horizontal_position*HMSdale.depth}.")
