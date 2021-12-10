import copy

with open("day10_input.txt") as d:
    data = [line.strip('\n') for line in d.readlines()]

test = ['[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]']

# ): 3
# ]: 57
# }: 1197
# >: 25137

pairs = ('()','[]','{}','<>')
openers = ['(','[','{','<']
closers = [')',']','}','>']

def remove_pairs(line):
    #returns line with immediately adjacent (),[],{},<> removed
    #and bool has_pairs if something has been removed
    #bool returns false when no more pairs to remove
    has_pairs = False
    to_remove = []
    
    for i in range(len(line)-1):
        if line[i]+line[i+1] in pairs:
            to_remove.append(line[i]+line[i+1])
            has_pairs = True
    for pair in to_remove:
        line = line.replace(pair,'')
    return(line,has_pairs)


def find_errors(line):
    #returns mismatched pair of brackets in line
    broken_opener = None
    illegal_char = None
    
    for i in range(len(line)-1):
        if line[i] in openers and line[i+1] in closers and line[i]+line[i+1] not in pairs:
            broken_opener = line[i]
            illegal_char = line[i+1]
    return(illegal_char, broken_opener)


def match(l_char):
    #returns closing bracket given opening bracket
    i = openers.index(l_char)
    return(closers[i])


def get_median(positions):
    return(positions[(len(positions)//2)])


#test
##for i in range(len(test)):
##    has_errors = True
##    while has_errors == True:
##        #print(line)
##        test[i], has_errors = remove_pairs(test[i])
##
##illegal_chars = []
##for line in test:
##    illegal_chars.append(find_errors(line)[0])
##
##error_score = 0
##for char in illegal_chars:
##    if char == ')':
##        error_score += 3
##    if char == ']':
##        error_score += 57
##    if char == '}':
##        error_score += 1197
##    if char == '>':
##        error_score += 25137


#part 1
data_part1 = copy.deepcopy(data)

#remove all complete (),[],{},<> from all entries
#until corrupted entries have their mismatched pair adjacent
#or incomplete entry is left with only lefties
for i in range(len(data_part1)):
    has_pairs = True
    while has_pairs == True:
        data_part1[i], has_pairs = remove_pairs(data_part1[i])

#adds illegal chars (incorrect right brackets) to list
#if entry is incomplete rather than corrupted, nothing is added
illegal_chars = []
for line in data_part1:
    illegal_chars.append(find_errors(line)[0])

#calculate error score
error_score = 0
for char in illegal_chars:
    if char == ')':
        error_score += 3
    if char == ']':
        error_score += 57
    if char == '}':
        error_score += 1197
    if char == '>':
        error_score += 25137

print(f"error score = {error_score}")


#part 2

# ): 1 
# ]: 2
# }: 3
# >: 4

data_part2a = copy.deepcopy(data)
data_part2b = []

#strip data_part2a entries down as in part 1
for i in range(len(data_part2a)):
    
    has_pairs = True
    
    while has_pairs == True:
        data_part2a[i], has_pairs = remove_pairs(data_part2a[i])
        
    #if entry is not corrupted
    if set(find_errors(data_part2a[i])) == set([None]): 
        data_part2b.append(data_part2a[i])
    #data_part2b is all uncorrupted entries stripped of pairs

#calculate completion scores
completion_scores = []

for entry in data_part2b:
    lefties = []
    for char in entry:
        if char in openers:
            lefties.append(char)

    righties = []
    lefties.reverse()
    for char in lefties:
        righties.append(match(char))
    
    entry_score = 0
    for char in righties:
        if char == ')':
            value = 1
        if char == ']':
            value = 2
        if char == '}':
            value = 3
        if char == '>':
            value = 4
        entry_score = entry_score*5 + value
        
    completion_scores.append(entry_score)

completion_scores.sort()
print(f"median score = {get_median(completion_scores)}")






