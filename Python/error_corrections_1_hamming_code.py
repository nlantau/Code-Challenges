# nlantau, 2021-02-07

# Completed

import re



def encode(s):
    ascii_list = list()
    binary_list = list()
    hammed_words = list()
    for letter in s:
        # ASCII
        ascii_list.append(ord(letter))

        # Binary
        bin_val = ""
        bin_val = f'{ord(letter):b}'
        while len(bin_val) < 8:
            bin_val = "0" + bin_val
        binary_list.append(bin_val)

        # Hamming Encode
        hammed_digits = list()
        for digit in bin_val:
            if digit == '0':
                hammed_digits.append('000')
            else:
                hammed_digits.append('111')
        hammed_words.append("".join(hammed_digits))
    return "".join(hammed_words)
       

def decode(b):
    triplet_list = re.findall(r'\d{3}', b)

    decoded_str = ""

    for trp in triplet_list:
        if int(trp) == 111:
            decoded_str += '1'
        elif int(trp) == 0:
            decoded_str += '0'
        else:
            one = 0
            two = 0
            for ch in trp:
                if ch == '1':
                    one += 1
                else:
                    two += 1
            if one > two:
                decoded_str += '1'
            else:
                decoded_str += '0'

    bytes_list = re.findall(r'\d{8}', decoded_str)

    return "".join([chr(int(x,2)) for x in bytes_list])


t = "000111111000111000000000000111111000000111000111000111111111111000000111" 
print(encode("hey"))
print(decode(t))
