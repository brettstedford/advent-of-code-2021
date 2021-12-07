from common import get_input_as_lines

def get_signficant_bit(data:list[str], bit_pos: int, type: str='most'):
    high = 0
    low = 0
    
    for _, val in enumerate(data):
        bit = int(list(val)[bit_pos])
        if(bit == 0):
            low+=1
        
        if(bit == 1):
            high+=1

    if(high > low or high == low):
        return 1 if type == "most" else 0
    
    if(low > high):
        return 0 if type == "most" else 1

def filter_by_bit_at_pos(data:list[str], bit_pos:int, sig_bit:int):
    f = filter(lambda bits: int(list(bits)[bit_pos]) == sig_bit, data)
    return list(f)


lines: list[str] = get_input_as_lines('day3')

oxy_gen_rating: list[str] = lines
c02_scrubber_rating: list[str] = lines

data_len = len(lines[0])

for i in range(0, data_len):
    ogr_sig_bit = get_signficant_bit(oxy_gen_rating, i)
    cs_sig_bit = get_signficant_bit(c02_scrubber_rating, i, 'least')
    
    print(i)
    print('oxy', ogr_sig_bit)
    print('c02', cs_sig_bit)

    if(len(oxy_gen_rating) > 1):
        oxy_gen_rating = filter_by_bit_at_pos(oxy_gen_rating, i, ogr_sig_bit)
    
    if(len(c02_scrubber_rating) > 1):
        c02_scrubber_rating = filter_by_bit_at_pos(c02_scrubber_rating, i, cs_sig_bit)

ls_rating = int(oxy_gen_rating[0], 2) * int(c02_scrubber_rating[0], 2)

print(ls_rating)
