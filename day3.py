from common import get_input_as_lines

lines: list[str] = get_input_as_lines('day3')

gamma_binary = ''
epsilon_binary = ''

data_len = len(lines[0])

for i in range(0, data_len):
    high = 0
    low = 0
    
    for j, val in enumerate(lines):
        bit = int(list(val)[i])
        if(bit == 0):
            low+=1
        
        if(bit == 1):
            high+=1

    if(high > low):
        gamma_binary += '1'
        epsilon_binary += '0'
    
    if(low > high):
        gamma_binary += '0'
        epsilon_binary += '1'

gamma_rate = int(gamma_binary, 2)
epsilon_rate = int(epsilon_binary, 2)

print(gamma_binary, '>>>', gamma_rate)
print(epsilon_binary, '>>>', epsilon_rate)
print(gamma_rate, '*', epsilon_rate, '>>>', gamma_rate * epsilon_rate)