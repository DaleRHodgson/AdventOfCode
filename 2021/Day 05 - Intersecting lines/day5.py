from itertools import product

with open("day5_input.txt") as d:
    data = [[(int(a),int(b)),(int(c),int(d))] for a,b,c,d  in [ line.strip('\n').replace('->',',').split(',') for line in d.readlines() ]]

with open("day5_test.txt") as ddd:
    test = [[(int(a),int(b)),(int(c),int(d))] for a,b,c,d  in [ line.strip('\n').replace('->',',').split(',') for line in ddd.readlines() ]]

test_board = [[0 for i in range(10)] for j in range(10)]


def show_test():
    for i in range(10):
        print(test_board[i])
    
#### test
##nondiag_lines_test = []
##diag_lines_test = []
##for entry in test:
##    if entry[0][0] == entry[1][0] or entry[0][1] == entry[1][1]:
##        nondiag_lines_test.append(entry)
##    else:
##        diag_lines_test.append(entry)


nondiag_lines = []
diag_lines = []
for entry in data:
    if entry[0][0] == entry[1][0] or entry[0][1] == entry[1][1]:
        nondiag_lines.append(entry)
    else:
        diag_lines.append(entry)


#### Part 1
# mark all horizontal and vertical lines on board,
# count number of points where at least two lines overlap
        
def part1():

    # create 1000x1000 array of all 0 entries
    # to represent board
    board = [[0 for i in range(1000)] for j in range(1000)]
    
    for line in nondiag_lines:
        x1 = min(line[0][0],line[1][0])
        x2 = max(line[0][0],line[1][0])
        y1 = min(line[0][1],line[1][1])
        y2 = max(line[0][1],line[1][1])

        # make list of all points on line:
        hits = [ (x,y) for x in range(x1,x2+1) for y in range(y1,y2+1) ]

        # mark board by +1 on these points
        for a,b in hits:
            board[b][a] += 1

    # find danger_points as anywhere on board marked greater than 1
    danger_points = 0
    for a,b in [(i,j) for i in range(1000) for j in range(1000)]:
        if board[b][a] > 1:
            danger_points += 1

    print(f"{danger_points} danger points")

print('==== Part 1 ====')
part1()


#### Part 2
# as above, including diagonal lines

def part2():

    # create 'empty' board
    board = [[0 for i in range(1000)] for j in range(1000)]

    # count of commands to run
    num_commands = len(data)
    
    # mark non diagonal lines as above
    for line in nondiag_lines:
        x1 = min(line[0][0],line[1][0])
        x2 = max(line[0][0],line[1][0])
        y1 = min(line[0][1],line[1][1])
        y2 = max(line[0][1],line[1][1])
        hits = [ (x,y) for x in range(x1,x2+1) for y in range(y1,y2+1) ]
        for a,b in hits:
            board[b][a] += 1
        num_commands -= 1
        print(f"{num_commands} lines remaining")

    # mark diagonal lines
    for line in diag_lines:
        (x1,y1) = (line[0][0],line[0][1])
        (x2,y2) = (line[1][0],line[1][1])

        # gradient and offset of line
        m = int((y2-y1)/(x2-x1))
        c = y1 - m*x1

        # for every point between (x1,y1) and (x2,y2), check if it lies on this diagonal;
        # mark as appropriate
        for a,b in [(i,j) for i in range(min(x1,x2),max(x1,x2)+1) for j in range(min(y1,y2),max(y1,y2)+1)]:
            if b == m*a+c: 
                board[b][a] += 1
        num_commands -= 1
        print(f"{num_commands} lines remaining")

    # count danger points as previous
    danger_points = 0
    for a,b in [(i,j) for i in range(1000) for j in range(1000)]:
        if board[b][a] > 1:
            danger_points += 1

    print(f"{danger_points} danger points")

print('\n=== Part 2 ====')
part2()

################ ################ 
## Part 2 runs slow due to checking many board points to see if they
## lie on a given diagonal.
##
## This could be optimised by instead making a list of hits (as with
## non diagonals). i.e. identify which direction (x2,y2) is from (x1,y1)
## and fill a list of the points in between.
##
## Current implementation will work for lines at any angle (not just 45deg.
