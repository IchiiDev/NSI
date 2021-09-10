def bunny(n):
    if n == 1 or n == 0: return 1
    return bunny(n - 1) + bunny(n - 2)

def calc_evolution(n):
    if n == 1 or n == 0: return 1
    r1 = bunny(n-1)
    r2 = bunny(n-2)
    r = r1 + r2
    print((r - r1)/r1)
    calc_evolution(n-1)

calc_evolution(100)