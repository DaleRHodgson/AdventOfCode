with open("day8_input.txt") as d:
    #load entries as list of
    #{ 'clue': ['bcedagf', 'ebadf', 'gcdfe', 'gfcead', 'bcedgf', 'dfeca', 'ac', 'dgca', 'ace', 'cafbge'],
    #  'output': ['ecfdbag', 'gecfd', 'feadb', 'degacbf'] }
    data = [{'clue':a.split(' '), 'output':b.split(' ')} for a,b in [entry.strip('\n').split(' | ') for entry in d.readlines()]] 

## fig  |   segments    |    unique?
#  0    |   6
#  1    |   2               y
#  2    |   5
#  3    |   5
#  4    |   4               y
#  5    |   5
#  6    |   6
#  7    |   3               y
#  8    |   7               y
#  9    |   6


#part 1

#count 1,4,7,8
counts = 0
for line in data:
    for entry in line['output']:
        if len(entry) in [2,4,3,7]:
            counts += 1

print(f"{counts} uses of 1,4,7,8")


#part 2

def key_maker(input_clue):
    #given ['bcedagf', 'ebadf', 'gcdfe', 'gfcead', 'bcedgf', 'dfeca', 'ac', 'dgca', 'ace', 'cafbge']
    #returns dict of keys:    
    #where A is mapped from .., B is mapped from...
    key = {'A':None,
       'B':None,
       'C':None,
       'D':None,
       'E':None,
       'F':None,
       'G':None
       }
    one = None
    four = None
    seven = None
    eight = None

    six_lengths = []
    five_lengths = []

    for entry in input_clue:
        if len(entry) == 2:
            one = set(entry)
        if len(entry) == 4:
            four = set(entry)
        if len(entry) == 3:
            seven = set(entry)
        if len(entry) == 7:
            eight = set(entry)
        if len(entry) == 6 and entry not in six_lengths:
            six_lengths.append(entry)
        if len(entry) == 5 and entry not in five_lengths:
            five_lengths.append(entry)

    six_lens_intersection = set(six_lengths[0]).intersection(set(six_lengths[1]),set(six_lengths[2])) #n6s
    five_lens_intersection= set(five_lengths[0]).intersection(set(five_lengths[1]),set(five_lengths[2])) #n5s

    key['A'] = list(seven.difference(one))[0] #7-1 is top
    key['F'] = list(one.intersection(six_lens_intersection))[0] #1n(n6s) is bottomright
    key['C'] = list(one.difference({key['F']}))[0] #topright is 1n(bottomright)
    key['G'] = list(five_lens_intersection.intersection(six_lens_intersection).difference(set(key['A'])))[0] #bottom is (n5s)n(n6s)-top
    key['D'] = list(five_lens_intersection.difference(six_lens_intersection))[0] #middle is (n5s)-n6s
    key['B'] = list(four.difference(one.union({key['D']})))[0] #topleft is 4-(1u(middle))
    key['G'] = list(five_lens_intersection.difference({key['D']}.union({key['A']})))[0] #bottom is (n5s)-middle-top
    key['E'] = list({'a','b','c','d','e','f','g'}.difference(set(key.values())))[0]

    return(key)
    

def decoder(input_code, key):
    #given ['ecfdbag', 'gecfd', 'feadb', 'degacbf'], and key (dictionary)
    #returns ['DAGBEFC', 'CDAGB', 'GDFBE', 'BDCFAEG']
    
    decoded = []

    for entry in input_code:
        for char in key.keys():
            entry = entry.replace(key[char],char)
        decoded.append(entry)
    
    return(decoded)
    
def display_to_num(code_list):
    #given ['DAGBEFC', 'CDAGB', 'GDFBE', 'BDCFAEG']
    #returns [5,3,5,3]
    
    list_out = []
    for entry in code_list:
        if set(entry) == set('ABCEFG'):
            list_out.append(0)
        elif set(entry) == set('CF'):
            list_out.append(1)
        elif set(entry) == set('ACDEG'):
            list_out.append(2)
        elif set(entry) == set('ACDFG'):
            list_out.append(3)
        elif set(entry) == set('BCDF'):
            list_out.append(4)
        elif set(entry) == set('ABDFG'):
            list_out.append(5)
        elif set(entry) == set('ABDEFG'):
            list_out.append(6)
        elif set(entry) == set('ACF'):
            list_out.append(7)
        elif set(entry) == set('ABCDEFG'):
            list_out.append(8)
        elif set(entry) == set('ABCDFG'):
            list_out.append(9)
        else:
            print("ERROR", entry)
            break
    return(list_out)
            

nums_out = []
for entry in data:
    key = key_maker(entry['clue'])
    decoded = display_to_num(decoder(entry['output'],key))
    nums_out.append(sum([decoded[i]*(10**(4-i-1)) for i in range(4)])) #sums powers of 10 to turn [5,3,5,3] into 5353 (int)
print(f"sum of decoded nums = {sum(nums_out)}")
    
