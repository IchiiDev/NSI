def puissance(x, n):
    if n == 0: return 1
    return x * puissance(x, n-1)

def puissance2(x, n):
    if n == 0: return 1
    if n % 2 == 0: 
        r = puissance2(x, n/2)
        return r**2
    else:
        r = puissance2(x, (n-1)/2)
        return x * r**2

"""
listex = [10, 0.5, -0.3, -5, 1, 0]
listen = [0, 1, 2, 3, 4]

print("x\tn\tx^n")
for n in listen: 
    for x in listex: print(f"{x}\t{n}\t{puissance(x, n)}")
"""

print(puissance2(3, 4))
