def echiquier(n):
    if n == 0: return 1
    return echiquier(n - 1) + 2**n

def calc_max_weight(n):
    return (echiquier(n) * 0.04) / 1000

def echiquier2(n):
    if n == 0: 
        print(f"Total\t2**n\n1\t1")
        return 1
    result = echiquier2(n - 1) + 2**n
    print(f"{result}\t{2**n}")
    return result

# print(f"{(calc_max_weight(63) / 1000) / 450000000 }y")
echiquier2(63)