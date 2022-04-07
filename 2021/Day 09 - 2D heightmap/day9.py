with open("day9_input.txt") as d:
    data = [line.strip('\n') for line in d.readlines()]

data_array = [ [int(char) for char in data[i]] for i in range(0,len(data)) ]

test = [[2,1,9,9,9,4,3,2,1,0],
        [3,9,8,7,8,9,4,9,2,1],
        [9,8,5,6,7,8,9,8,9,2],
        [8,7,6,7,8,9,6,7,8,9],
        [9,8,9,9,9,6,5,6,7,8]]

test_data = {(x,y):test[y][x] for y in range(5)
             for x in range(10)
             }

data_board = {(x,y):data_array[y][x] for y in range(len(data_array))
             for x in range(len(data_array[0]))
             }


def get_nbrs(_pt):
    h_max = len(data_array[0])-1
    v_max = len(data_array)-1

    #for testing
    #h_max = len(test[0])-1
    #v_max = len(test)-1
    
    #nbrs= [U,R,D,L]
    nbrs = set([(_pt[0],abs(_pt[1]-1)),
                (min(_pt[0]+1,h_max),_pt[1]),
                (_pt[0],min(_pt[1]+1,v_max)),
                (abs(_pt[0]-1),_pt[1])])
    nbrs = nbrs.difference({pt}) #remove pt itslf
    return(nbrs)

def is_low_pt(pt,seafloor):
    #pt = (x,y)

    nbrs = get_nbrs(pt)

    #print(pt,test_data[pt])

    #list of bools
    nbrs_are_higher = [seafloor[nbr] > seafloor[pt] for nbr in nbrs]

    #if all are true (higher), then we have low pt
    if sum(nbrs_are_higher) == len(nbrs_are_higher):
        return(True)
    else:
        return(False)

#for pt:
# if is_low_pt(pt):
#  danger_points.append(pt)

#test
##low_points = []
##risk_levels = []
##for pt in test_data.keys():
##    if is_low_pt(pt,test_data):
##        low_points.append(pt)
##        risk_levels.append(test_data[pt]+1)

#real part1
low_points = []
risk_levels = []
for pt in data_board.keys():
    if is_low_pt(pt,data_board):
        low_points.append(pt)
        risk_levels.append(data_board[pt]+1)

#part 1
print(f"sum of risk levels = {sum(risk_levels)}")


#basin_centres_test = {low_pt:test_data[low_pt] for low_pt in low_points}
basin_centres = {low_pt:data_board[low_pt] for low_pt in low_points}

#basins_test = [[(centre_pt,basin_centres_test[centre_pt])] for centre_pt in basin_centres_test.keys()]
basins = [[(centre_pt,basin_centres[centre_pt])] for centre_pt in basin_centres.keys()]

#test
##for basin in basins_test:
##    for pt in basin:
##        nbrs = get_nbrs(pt[0])
##        for nbr in nbrs:
##            if test_data[nbr] > test_data[pt[0]] and test_data[nbr] != 9 and nbr not in basin:
##                basin.append((nbr,test_data[nbr]))
##for i in range(len(basins_test)):
##    basins_test[i] = set(basins_test[i])

#real
for basin in basins:
    for pt in basin:
        nbrs = get_nbrs(pt[0])
        for nbr in nbrs:
            if data_board[nbr] > data_board[pt[0]] and data_board[nbr] != 9 and nbr not in basin:
                basin.append((nbr,data_board[nbr]))
for i in range(len(basins)):
    basins[i] = set(basins[i])

#basin_test_sizes = [len(basin) for basin in basins_test]
basin_sizes = [len(basin) for basin in basins]


while len(basin_sizes) > 3:
    basin_sizes.remove(min(basin_sizes))

print(f"product of largest basins = {basin_sizes[0]*basin_sizes[1]*basin_sizes[2]}")
