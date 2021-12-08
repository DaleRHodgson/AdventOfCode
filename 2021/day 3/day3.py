with open("day3_input.txt") as d:
    data = [line.strip('\n') for line in d.readlines()]

# Turn input data into a list of lists of integers
data_array = [ [int(char) for char in data[i]] for i in range(1,len(data)) ]


gamma_rate_array = []


#find gamma rate
for i in range(12):
    gamma_bit_count = sum([data_array[j][i] for j in range(len(data_array))])
# if sum of bits in column is greater than half the length of the data,
# then 1 is more common than 0 in that column:
    if gamma_bit_count > len(data_array)/2: 
        gamma_rate_array.append(1)
    else:
        gamma_rate_array.append(0)


# epsilon rate is inverse of gamma rate    
epsilon_rate_array = [(bit+1)%2 for bit in gamma_rate_array]

#concatenate lists of bits into str so so int works and can do arithmatic
gamma_str = ''
for bit in gamma_rate_array:
    gamma_str = gamma_str + str(bit)

epsilon_str = ''
for bit in epsilon_rate_array:
    epsilon_str = epsilon_str + str(bit)


print(f"The product of gamma rate and epsilon rate is {int(gamma_str,2)*int(epsilon_str,2)}.")


# part 2

#practice data
data_copy = [[0,0,1,0,0],
            [1,1,1,1,0],
            [1,0,1,1,0],
            [1,0,1,1,1],
            [1,0,1,0,1],
            [0,1,1,1,1],
            [0,0,1,1,1],
            [1,1,1,0,0],
            [1,0,0,0,0],
            [1,1,0,0,1],
            [0,0,0,1,0],
            [0,1,0,1,0]]

data_copy_ox = data_array
data_copy_CO2 = data_array

for i in range(12):
    #what is most common bit in ith place? = key_bit
    #make a new list of all entries where the key_bit is right
    #overwrite starting list with filtered list
    #repeat until just a single value remains

    bit_count_ox = sum([data_copy_ox[j][i] for j in range(len(data_copy_ox))])
    
    if bit_count_ox >= len(data_copy_ox)/2:
        key_bit_ox = 1
    else:
        key_bit_ox = 0

    filtered_data_ox = []

    for entry in data_copy_ox:
        if entry[i] == key_bit_ox:
            filtered_data_ox.append(entry)

    data_copy_ox = filtered_data_ox

    if len(data_copy_ox) == 1:
        break
    
#same again
for i in range(12):
    bit_count_CO2 = sum([data_copy_CO2[j][i] for j in range(len(data_copy_CO2))])
    if bit_count_CO2 >= len(data_copy_CO2)/2:
        key_bit_CO2 = 0
    else:
        key_bit_CO2 = 1
    filtered_data_CO2 = []
    for entry in data_copy_CO2:
        if entry[i] == key_bit_CO2:
            filtered_data_CO2.append(entry)
    data_copy_CO2 = filtered_data_CO2
    if len(data_copy_CO2) == 1:
        break


#turn lists into strings again
ox_rating_str = ''
for bit in data_copy_ox[0]:
    ox_rating_str = ox_rating_str + str(bit)

CO2_rating_str = ''
for bit in data_copy_CO2[0]:
    CO2_rating_str = CO2_rating_str + str(bit)


print(f"The product of oxygen rating and CO2 rating is {int(ox_rating_str,2)*int(CO2_rating_str,2)}.")
