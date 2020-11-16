# Date: 16/11/2020

def ASCII(char_value):
    table = []
    for i in char_value:
        table.append(hex(ord(i)))
    return table

# Was a joke with my teacher to see wich one would do the weirdest code. I know this can be even worse.
def ASCIIFromTable(hex_values):
    for i in hex_values:
        hex_values[hex_values.index(i)] = chr(i)
    return "".join(hex_values)


print(ASCIIFromTable([0x42, 0x6f, 0x6e, 
                      0x6a, 0x6f, 0x75, 
                      0x72, 0x20, 0x74, 
                      0x6f, 0x75, 0x74,
                      0x20, 0x6c, 0x65, 
                      0x20, 0x6d, 0x6f, 
                      0x6e, 0x64, 0x65]))
