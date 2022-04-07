import copy

with open("day12_input.txt") as d:
    routes = [set(tuple(caves.split('-'))) for caves in [line.strip('\n') for line in d.readlines()]]

caves = set.union(*routes)

test1_routes = [set(('start','A')),
         set(('start','b')),
         set(('A','c')),
         set(('A','b')),
         set(('b','d')),
         set(('A','end')),
         set(('b','end'))]
test1_caves = set.union(*test1_routes)

test2_routes = [set(('dc','end')),
                set(('HN','start')),
                set(('start','kj')),
                set(('dc','start')),
                set(('dc','HN')),
                set(('LN','dc')),
                set(('HN','end')),
                set(('kj','sa')),
                set(('kj','HN')),
                set(('kj','dc'))]
test2_caves = set.union(*test2_routes)

test3_routes = [set(('fs','end')),
         set(('he','DX')),
         set(('fs','he')),
         set(('start','DX')),
         set(('pj','DX')),
         set(('end','zg')),
         set(('zg','sl')),
         set(('zg','pj')),
         set(('pj','he')),
         set(('RW','he')),
         set(('fs','DX')),
         set(('pj','RW')),
         set(('zg','RW')),
         set(('start','pj')),
         set(('he','WI')),
         set(('zg','he')),
         set(('pj','fs')),
         set(('start','RW'))]
test3_caves = set.union(*test3_routes)

## For testing:
#caves = test1_caves
#routes = test1_routes

#caves = test2_caves
#routes = test2_routes

#caves = test3_caves
#routes = test3_routes
##


#### Part 1
# caves = set of strings of cave names
# routes = list of two-element sets, a set e.g. {'cz', 'WR'} indicates
# there exists a route between small cave 'cz' and large cave 'WR'.
#
# How many paths are there from cave 'start' to cave 'end' that visit
# small caves at most once?

# List to be populated with lists of valid paths
paths = [ ['start'] ]

# Method to extend {paths} list with new valid routes:
def extend_paths(_paths=paths, _routes=routes):
        new_paths = []
        for path in _paths:
                # Find current 'final' cave in route
                # if final cave is 'end', path is complete and added to new_paths
                # otherwise new_paths is appended with every possible extension
                # from {extent}
                extent = path[-1]
                if extent == 'end':
                        new_paths.append(path)
                else:
                        for cave in caves:
                                if set((extent,cave)) in _routes and (cave.isupper() or (cave.islower() and cave not in path) or (cave == 'end') ):
                                        new_paths.append(path+[cave])
        return(new_paths)

# Keep using extend_paths() method to add to {paths}
# until the length of {paths} does not increase (indicating
# that no more paths can be found).
more_paths_to_find = True
while more_paths_to_find == True:
        num_paths = len(paths)
        paths = extend_paths(paths)
        if len(paths) == num_paths: #more paths have not been added
                more_paths_to_find = False

print("==== PART 1 ====")
print(f"{len(paths)} paths found\n")



#### Part 2
# How many possible routes from 'start' to 'end' where:
# big caves can be visited any number of times,
# a single small cave can be visited at most twice,
# all other small caves can be visited at most once.

# A new list to fill with valid paths.
paths2 = [ ['start'] ]

# A new method to extend {paths2} with new validation rules:
def extend_paths2(_paths=paths2, _routes=routes):
        new_paths = []
        for path in _paths:                
                extent = path[-1]             
                if extent == 'end':
                        new_paths.append(path)
                else:
                        for cave in caves.difference({'start'}):
                                # Pick a {cave} to check validity of.
                                                 
                                valid_route = (set((extent,cave)) in _routes)
                                cave_is_big = cave.isupper()
                                cave_is_small = cave.islower() and cave != 'end'

                                # Has there been any double visits?
                                double_visited = None
                                if cave_is_small == True:
                                        visited_caves = set(path).difference({'start'})
                                        double_visited = False
                                        for visited_cave in visited_caves:
                                                if visited_cave.islower():
                                                        num_visits = path.count(visited_cave)
                                                        if num_visits >= 2:
                                                                double_visited = True
                                                        
                                # If yes, was it _this_ cave?
                                # cave will be valid _and_ small if there has been no double visits,
                                # or there has been a double visit to a cave which is not this one.
                                cave_is_valid_small = None
                                if cave_is_small == True and double_visited == True:
                                        this_cave_visits = path.count(cave)
                                        if this_cave_visits < 1:
                                                cave_is_valid_small = True
                                        elif this_cave_visits >= 1:
                                                cave_is_valid_small = False
                                if cave_is_small == True and double_visited == False:
                                        cave_is_valid_small = True

                                # A valid small cave may be added to the route.
                                if valid_route and cave_is_valid_small:
                                        new_path = path+[cave]
                                        new_paths.append(new_path)

                                # Big caves and 'end' are always valid.
                                if valid_route and (cave_is_big or cave == 'end'):
                                        new_path = path+[cave]
                                        new_paths.append(new_path)
        return(new_paths)

# Loop to completion as before:
more_paths_to_find = True
while more_paths_to_find == True:
        num_paths = len(paths2)
        paths2 = extend_paths2(paths2)
        if len(paths2) == num_paths: #more paths have not been added
                more_paths_to_find = False

print("==== PART 2 ====")
print(f"{len(paths2)} paths found\n")
