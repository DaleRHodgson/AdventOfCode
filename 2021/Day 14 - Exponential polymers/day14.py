import copy

with open("day14_input.txt") as d:
    raw_input = [line.strip('\n') for line in d.readlines()]

starting_polymer = raw_input[0]
pair_rules = [ line.split(' -> ') for line in raw_input[2:] ]

pair_insertion = { entry[0]:entry[1] for entry in pair_rules }
    

starting_test = 'NNCB'

test = {'CH': 'B',
        'HH': 'N',
        'CB': 'H',
        'NH': 'C',
        'HB': 'C',
        'HC': 'B',
        'HN': 'C',
        'NN': 'C',
        'BH': 'H',
        'NC': 'B',
        'NB': 'B',
        'BN': 'B',
        'BB': 'N',
        'BC': 'B',
        'CC': 'N',
        'CN': 'C'}

#pair_insertion = test
#starting_polymer = starting_test


#setup num_pairs dict from starting_polymer
num_pairs = {pair: 0 for pair in pair_insertion.keys()}
#count actual pairs:
for i in range(len(starting_polymer)-1):
        pair = starting_polymer[i] + starting_polymer[i+1]
        num_pairs[pair] += 1


#setup transformation_dict from pair_insertion
#                     { pair: [makes these pairs] , ...}
transformation_dict = {pair: None for pair in pair_insertion.keys()}
for pair in transformation_dict.keys():

        polymer = [pair[0], pair[1]]
        produces = pair_insertion[pair]
        pairs_produced = ( polymer[0]+produces, produces+polymer[1] )
        transformation_dict[pair] = pairs_produced


def grow_polymers(_num_pairs, _pair_insertion, _transformation_dict):
        new_pairs = {pair: 0 for pair in _pair_insertion.keys()}
        #for pair makes [p1,p2]:
        #num new p1 += num old pair; num new p2 += num old pair
        for polymers_produced in _transformation_dict.items():
                old_polymer = polymers_produced[0]
                new_polymer1 = polymers_produced[1][0]
                new_polymer2 = polymers_produced[1][1]
                new_pairs[new_polymer1] += _num_pairs[old_polymer]
                new_pairs[new_polymer2] += _num_pairs[old_polymer]
        #this bit works!
        return(new_pairs)

def count_polymers(_num_pairs):
        polymer_counts = {}
        
        #find individual polymers:
        for polymer_pair in _num_pairs.keys():
                if polymer_pair[0] not in polymer_counts.keys():
                        polymer_counts.update( {polymer_pair[0]:0} )

        for polymer in polymer_counts.keys():
                #count both first of pairs and last of pairs
                count_firsts = 0
                count_lasts = 0
                for entry in _num_pairs.items():
                        polymer_pair = entry[0]
                        count_pairs = entry[1]
                        if polymer_pair[0] == polymer:
                                count_firsts += count_pairs
                        if polymer_pair[1] == polymer:
                                count_lasts += count_pairs
                #                               #and compare because start of chain/end of chain
                #                               #will have +- 1 error
                polymer_counts.update( {polymer: max(count_firsts, count_lasts)} )
        
        return(polymer_counts)

        


#### PART 1 ####
print("==== PART 1 ====\n")
for i in range(10):
        num_pairs = grow_polymers(num_pairs, pair_insertion, transformation_dict)

poly_counts = count_polymers(num_pairs)
print(poly_counts)
highest_count = max(poly_counts.values())
lowest_count = min(poly_counts.values())
most_common = list(poly_counts.keys())[list(poly_counts.values()).index(highest_count)]
least_common = list(poly_counts.keys())[list(poly_counts.values()).index(lowest_count)]
print(f"Most common ({most_common}) {highest_count} - least common ({least_common}) {lowest_count} = {highest_count-lowest_count}")


#### PART 2 ####
print("==== PART 2 ====\n")
for i in range(30):
        num_pairs = grow_polymers(num_pairs, pair_insertion, transformation_dict)

poly_counts = count_polymers(num_pairs)
print(poly_counts)
highest_count = max(poly_counts.values())
lowest_count = min(poly_counts.values())
most_common = list(poly_counts.keys())[list(poly_counts.values()).index(highest_count)]
least_common = list(poly_counts.keys())[list(poly_counts.values()).index(lowest_count)]
print(f"Most common ({most_common}) {highest_count} - least common ({least_common}) {lowest_count} = {highest_count-lowest_count}")
