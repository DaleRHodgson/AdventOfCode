with open("day3_input.txt") as d:
    data = [line.strip('\n') for line in d.readlines()]

# Turn input data into a list of lists of integers
data_array = [ [int(char) for char in data[i]] for i in range(1,len(data)) ]


#### Part 1
# calculate power rate from (gamme_rate * epsilon_rate)
# gamma_rate is most common bits in each position
# epsilon_rate is least common bits in each position


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

#concatenate lists of bits into str so int works and can do arithmetic
gamma_str = ''
for bit in gamma_rate_array:
    gamma_str = gamma_str + str(bit)

epsilon_str = ''
for bit in epsilon_rate_array:
    epsilon_str = epsilon_str + str(bit)


print(f"The product of gamma rate and epsilon rate is {int(gamma_str,2)*int(epsilon_str,2)}.")


#### Part 2
# calculate life support rating as (ox_rating * CO2_rating)
# ox_rating: filter data by keeping entries where each bit = the most common bit
# in that column.
# CO2_rating: filter data by keeping entries where each bit = least common bit
# in that column.


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

# calculate ox_rating
for i in range(12):
    #what is most common bit in ith place? = key_bit
    #make a new list of all entries where the key_bit is right
    #overwrite starting list with filtered list
    #repeat until just a single value remains

    # calculate key_bit
    bit_count_ox = sum([data_copy_ox[j][i] for j in range(len(data_copy_ox))])
    if bit_count_ox >= len(data_copy_ox)/2:
        key_bit_ox = 1
    else:
        key_bit_ox = 0

    # filter by key_bit and overwrite lise
    filtered_data_ox = []
    for entry in data_copy_ox:
        if entry[i] == key_bit_ox:
            filtered_data_ox.append(entry)
    data_copy_ox = filtered_data_ox

    # check to see if we reach final entry
    if len(data_copy_ox) == 1:
        break
    
#same again fr CO2_rating
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
