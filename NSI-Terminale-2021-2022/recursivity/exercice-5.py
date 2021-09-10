def echiquier(n):
    if n == 0: return 0
    return echiquier(n - 1) + 2**n

def calc_max_weight(n):
    return (echiquier(n) * 0.04) / 1000

print(f"{(calc_max_weight(63) / 1000) / 450000000 }y")