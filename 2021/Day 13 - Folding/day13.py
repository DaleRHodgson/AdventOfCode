import copy

with open("day13_input.txt") as d:
    raw_input = [line.strip('\n') for line in d.readlines()]

splitting_pt = raw_input.index('')
coords = [ [int(x),int(y)] for x,y in [ d.split(',') for d in raw_input[:splitting_pt]]]
instructions = raw_input[splitting_pt+1:]

test_a = [[6,10],
        [0,14],
        [9,10],
        [0,3],
        [10,4],
        [4,11],
        [6,0],
        [6,12],
        [4,1],
        [0,13],
        [10,12],
        [3,4],
        [3,0],
        [8,4],
        [1,10],
        [2,14],
        [8,10],
        [9,0]]
test_b = ['fold along y=7', 'fold along x=5']

def read_instruction(line):
        equation = line.split(' ')[-1] #returns x=5 etc.
        folding_line = int(equation[2:])
        folding_up = (equation[0] == 'y')
        folding_left = (equation[0] == 'x')
        return(folding_line, folding_up, folding_left)


#### PART 1 ####

#coords = test_a
#instructions = test_b


folding_line, folding_up, folding_left = read_instruction(instructions[0])

def fold(_folding_line, _folding_up, _folding_left, _coords):

        #folding up
        if _folding_up == True:
                for coord in _coords:
                        if coord[1] > _folding_line:
                                coord = (coord[0], 2*_folding_line - coord[1])

        #folding left
        if _folding_left == True:
                for coord in _coords:
                        if coord[0] > _folding_line:
                                coord = ( 2*_folding_line - coord[0], coord[1])

        for coord in _coords:
                #folding up
                if _folding_up == True:
                        if coord[1] > _folding_line:
                                coord[1] = 2*_folding_line - coord[1]
                        
                #folding left
                if _folding_left == True:
                        if coord[0] > _folding_line:
                                coord[0] = 2*_folding_line - coord[0]
        return(_coords)

def count_dots(coords):
        list_of_tuples = [tuple(coord) for coord in coords]
        output_set = set(list_of_tuples)
        return(len(output_set))


coords = fold(folding_line, folding_up, folding_left, coords)
num_dots = count_dots(coords)


print(f"{num_dots} dots visible after first fold\n")


#### PART 2 ####

for instruction in instructions[1:]:
        folding_line, folding_up, folding_left = read_instruction(instruction)
        coords = fold(folding_line, folding_up, folding_left, coords)
        print(f"folded {instruction}\n")


def show_dots(_coords=coords):

        list_of_tuples = [tuple(coord) for coord in coords]
        output_set = set(list_of_tuples)
        _coords = output_set
        
        x_max = max( [ coord[0] for coord in _coords ] )+1
        y_max = max( [ coord[1] for coord in _coords ] )+1

        for y in range(y_max):
                #print horiz line
                line = [ '#' if [x,y] in coords else '.' for x in range(x_max)]
                display = ''
                for i in range(len(line)):
                        display += line[i]
                print(display)
                                                
                
show_dots(coords)

