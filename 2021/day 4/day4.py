import copy

with open("day4_input.txt") as d:
    random_nums = [ int(entry) for entry in d.readline().strip('\n').split(',') ]
    data = [line for line in d.readlines()]

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


class bingo_board:
    def __init__(self, _input_data):
        self.entries = copy.deepcopy(_input_data)
        self.score = 0

    def check_rows(self):
        #if sum <= -5 then win
        for row in self.entries:
            if sum(row) <= -5:
                print('BINGO!')
                self.count_score()
                print(f"Score: {self.score}")
                break

    def check_cols(self):
        for i in range(5):
            if sum([row[i] for row in self.entries]) <= -5:
                print('BINGO!')
                self.count_score()
                print(f"Score: {self.score}")
                break

    def check_card(self):
        self.check_rows()
        self.check_cols()

    def mark_num(self,called_num):
        #replace with -1
        for row in self.entries:
            for i in range(5):
                if row[i] == called_num:
                    row[i] = -1

    def count_score(self):
        #if +ve then sum
        for row in self.entries:
            for num in row:
                if num >= 0:
                    self.score += num
        return self.score

    def show(self):
        for i in range(5):
            print(self.entries[i])


def part1():

    # make list of bingo_board objects from card_data
    part1_cards = [bingo_board(card) for card in card_data]

    #run through randmo_nums marking boards until first winner
    for num in random_nums:
        for bingo_card in part1_cards:
            bingo_card.mark_num(num)
            bingo_card.check_card()
            card_score = bingo_card.score
            if card_score > 0:
                bingo_card.score = 0
                #bingo_card.show()
                last_num = num
                return(f"Last called number: {last_num}", f"First winner's score = {card_score*last_num}")

                    
print(part1())


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
                print(f"{len(part2_cards)} cards remaining.")

        # check for final winner
        if len(part2_cards) == 0:
            card_score = bingo_card.score
            last_num = num
            print('Final winner!')
            return(f"Last called number: {last_num}", f"Final winner's score = {card_score*last_num}")
  
print(part2())
