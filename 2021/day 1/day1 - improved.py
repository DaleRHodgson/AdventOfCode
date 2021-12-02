from numpy import loadtxt

with open('day1_input.txt') as data:
    data = loadtxt('day1_input.txt')

#part 1
num_increases = 0

for i in range(1,len(data)):
    change = data[i] - data[i-1]
    if change > 0:
        num_increases += 1

print(f"There are {num_increases} measurements that are larger than the previous measurement.")

#part 2
sliding_sums = [ data[i-2] + data[i-1] + data[i] for i in range(2,len(data))]

def count_changes(input_list):
    num_increases = 0

    for i in range(1,len(input_list)):
        if input_list[i] - input_list[i-1] > 0:
            num_increases += 1

    return num_increases

sliding_changes = count_changes(sliding_sums)

print(f"There are {sliding_changes} sums that are larger than the previous sum.")
