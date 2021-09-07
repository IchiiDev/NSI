def sRecProd(n):
    if n == 1: return 1
    else: return sRecProd(n - 1) * n

print(sRecProd(3))