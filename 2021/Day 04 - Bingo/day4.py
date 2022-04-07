import copy

with open("day4_input.txt") as d:
    random_nums = [ int(entry) for entry in d.readline().strip('\n').split(',') ]
    data = [line for line in d.readlines()]

## Handle input
data_copy = data
card_data = []

# turn input data into list of arrays
while len(data_copy) > 5:
    card = []
    first_break = data_copy.index('\n')
    next_break = first_break+5
    
    for entry in data_copy[ first_break+1 : next_break+1 ] :
        entry_nums = [int(entry.strip('\n')[i:i+2]) for i in range(0,13,3)]
        card.append(entry_nums)

    card_data.append(card) # add card to list
    data_copy = data_copy[next_break:] #remove used card
##


# Class to act as each bingo card
# instantiated with a 5x5 array of ints
# has methods to 'mark' numbers,
# to check for 'filled' rows and cols,
# and to calculate the cards 'score'
class bingo_board:
    def __init__(self, _input_data):
        self.entries = copy.deepcopy(_input_data)
        self.score = 0

    def mark_num(self,called_num):
        #'mark' a board by replacing the called number
        # with -1
        for row in self.entries:
            for i in range(5):
                if row[i] == called_num:
                    row[i] = -1

    def check_rows(self):
        # a completely 'marked' row is all '-1'
        # so if the sum of the row <= -5 we have a win
        for row in self.entries:
            if sum(row) <= -5:
                self.count_score()
                # For debugging:
                #print(f"BINGO!\nScore: {self.score}")
                break

    def check_cols(self):
        # as above
        # check to see if column sums <= -5
        for i in range(5):
            if sum([row[i] for row in self.entries]) <= -5:
                self.count_score()
                # For debugging:
                #print(f"BINGO!\nScore: {self.score}")
                break

    def check_card(self):
        self.check_rows()
        self.check_cols()

    def count_score(self):
        # sums all unmarked numbers to be used to find score
        # unmarked numbers will be >= 0
        for row in self.entries:
            for num in row:
                if num >= 0:
                    self.score += num
        return self.score

    def show(self):
        # method to display card for debugging
        for i in range(5):
            print(self.entries[i])

#### Part 1
# find which board wins first, calculate its score

def part1():

    # make list of bingo_board objects from card_data
    part1_cards = [bingo_board(card) for card in card_data]

    #run through random_nums, marking boards until first winner
    for num in random_nums:
        for bingo_card in part1_cards:
            bingo_card.mark_num(num)
            bingo_card.check_card()
            card_score = bingo_card.score

            # if .check_card() has found a winner then .score will be greater than 0
            if card_score > 0:
                # display for debugging:
                #bingo_card.show()
                last_num = num
                return(f"Last called number: {last_num}", f"First winner's score = {card_score*last_num}")

print('==== Part 1 ====')                    
print(part1())


#### Part 2
# find board which wins last, calculate its score

def part2():
    part2_cards = [bingo_board(card) for card in card_data]
    for num in random_nums:
        # pass to mark numbers
        for bingo_card in part2_cards:
            bingo_card.mark_num(num)
            bingo_card.check_card()
            
        # pass to remove winners
        for bingo_card in part2_cards:
            if bingo_card.score > 0:
                part2_cards.remove(bingo_card)
                # For debugging:
                #print(f"{len(part2_cards)} cards remaining.")

        # check for final winner
        if len(part2_cards) == 0:
            card_score = bingo_card.score
            last_num = num
            print('Final winner!')
            return(f"Last called number: {last_num}", f"Final winner's score = {card_score*last_num}")

print('\n==== Part 2 ====')
print(part2())
