def sIte1(n):
    s = 0
    for i in range(n):
        s = s + n
    return s

def sIte2(n):
    s = 0
    print(f"n\ts\n0\t{s}")
    for i in range(n):
        s = s + n
        print(f"{i + 1}\t{s}")

sIte2(13)