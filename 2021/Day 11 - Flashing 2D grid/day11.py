import copy

with open("day11_input.txt") as d:
    data = [line.strip('\n') for line in d.readlines()]

test = [[5,4,8,3,1,4,3,2,2,3],
        [2,7,4,5,8,5,4,7,1,1],
        [5,2,6,4,5,5,6,1,7,3],
        [6,1,4,1,3,3,6,1,4,6],
        [6,3,5,7,3,8,5,4,7,8],
        [4,1,6,7,5,2,4,6,4,5],
        [2,1,7,6,8,4,1,7,2,1],
        [6,8,8,2,8,8,1,1,3,4],
        [4,8,4,6,8,4,8,5,5,4],
        [5,2,8,3,7,5,1,5,2,6]]

test_board = {(x,y):{'energy_lv':test[y][x], 'has_flashed':False} for y in range(len(test))
             for x in range(len(test[0]))
             }

data_array = [ [int(char) for char in data[i]] for i in range(0,len(data)) ]
data_board = {(x,y):{'energy_lv':data_array[y][x], 'has_flashed':False} for y in range(len(data_array))
             for x in range(len(data_array[0]))
             }

num_flashes=0

def show_test():
        for y in range(10):
            print( [ test_board[(x,y)]['energy_lv'] for x in range(10)] )

def get_nbrs(_pt,array):
    h_max = len(array[0])-1
    v_max = len(array)-1
   
    #nbrs= [U,UR,R,DR,D,DL,L,UL]
    nbrs = set([( _pt[0],                abs(_pt[1]-1)       ), #U
                ( min(_pt[0]+1,h_max),   abs(_pt[1]-1)       ), #UR
                ( min(_pt[0]+1,h_max),   _pt[1]              ), #R
                ( min(_pt[0]+1,h_max),   min(_pt[1]+1,v_max) ), #RD
                ( _pt[0],                min(_pt[1]+1,v_max) ), #D
                ( abs(_pt[0]-1),         min(_pt[1]+1,v_max) ), #DL
                ( abs(_pt[0]-1),         _pt[1]              ), #L
                ( abs(_pt[0]-1),         abs(_pt[1]-1)       )])#UL
    nbrs = nbrs.difference({_pt}) #remove pt itslf
    return(nbrs)


def step_octos(board):

    global num_flashes

    #increase level of all
    for coords in board.keys():
        board[coords]['has_flashed'] = False #reset flash counts
        board[coords]['energy_lv'] += 1

    pts_to_flash = []

    #check for lv>9 and add to pts to flash
    def check_energy_lvs():
        for coords in board.keys():
            squid = board[coords]
            if squid['energy_lv'] > 9 and squid['has_flashed'] == False and coords not in pts_to_flash:
                pts_to_flash.append(coords)
        #print(pts_to_flash)

    def do_flashes(_pts_to_flash):
        num_flashes = 0
        for coords in _pts_to_flash:
            squid = board[coords]
            squid['energy_lv'] = 0
            squid['has_flashed'] = True
            num_flashes += 1
            nbrs = list(get_nbrs(coords,test))
            for pt in nbrs:
                if pt not in _pts_to_flash and board[pt]['has_flashed'] == False:
                    board[pt]['energy_lv'] += 1
        _pts_to_flash = []
        return(num_flashes)
                    
        
    check_energy_lvs()

    while len(pts_to_flash) != 0:
        new_flashes = do_flashes(pts_to_flash)
        num_flashes += new_flashes
        pts_to_flash = []
        check_energy_lvs()
        #print(pts_to_flash)

#part 1
data_board1 = copy.deepcopy(data_board)
for i in range(100):
        step_octos(data_board1)
        if sum([data_board1[coords]['energy_lv'] for coords in data_board1.keys()]) == 0:
                print(f"All flash at step {i}!")
                break
print(f"after 100 steps, there are {num_flashes} flashes.")

#part 2
data_board2 = copy.deepcopy(data_board)
dark = True
step = 0
while dark == True:
        step_octos(data_board2)
        step += 1
        if sum([data_board2[coords]['energy_lv'] for coords in data_board2.keys()]) == 0:
            dark = False
            print(f"All flash at step {step}!")

