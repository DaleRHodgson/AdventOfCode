from itertools import product

with open("day5_input.txt") as d:
    data = [[(int(a),int(b)),(int(c),int(d))] for a,b,c,d  in [ line.strip('\n').replace('->',',').split(',') for line in d.readlines() ]]


with open("day5_test.txt") as ddd:
    test = [[(int(a),int(b)),(int(c),int(d))] for a,b,c,d  in [ line.strip('\n').replace('->',',').split(',') for line in ddd.readlines() ]]

test_board = [[0 for i in range(10)] for j in range(10)]

def show_test():
    for i in range(10):
        print(test_board[i])
    
## test
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


#part1
        
def part1():

    board = [[0 for i in range(1000)] for j in range(1000)]
    
    for line in nondiag_lines:
        x1 = min(line[0][0],line[1][0])
        x2 = max(line[0][0],line[1][0])
        y1 = min(line[0][1],line[1][1])
        y2 = max(line[0][1],line[1][1])
        hits = [ (x,y) for x in range(x1,x2+1) for y in range(y1,y2+1) ]
        for a,b in hits:
            board[b][a] += 1
    
    danger_points = 0
    for a,b in [(i,j) for i in range(1000) for j in range(1000)]:
        if board[b][a] > 1:
            danger_points += 1

    print(f"{danger_points} danger points")


#part2

def part2():

    board = [[0 for i in range(1000)] for j in range(1000)]

    num_commands = len(data)
    
    #nondiag
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

    #diag
    for line in diag_lines:
        (x1,y1) = (line[0][0],line[0][1])
        (x2,y2) = (line[1][0],line[1][1])

        m = int((y2-y1)/(x2-x1))
        c = y1 - m*x1
        
        for a,b in [(i,j) for i in range(1000) for j in range(1000)]:
            if b == m*a+c and min(x1,x2)<=a<=max(x1,x2) and min(y1,y2)<=b<=max(y1,y2):
                board[b][a] += 1
        num_commands -= 1
        print(f"{num_commands} lines remaining")

    danger_points = 0
    for a,b in [(i,j) for i in range(1000) for j in range(1000)]:
        if board[b][a] > 1:
            danger_points += 1

    print(f"{danger_points} danger points")
