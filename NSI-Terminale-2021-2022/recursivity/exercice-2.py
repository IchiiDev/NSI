def sRec1(n):
    if n == 0:
        return 0
    else:
        return sRec1(n - 1) + n

def sRec2(n):
    if n == 0:
        print(f"n\ts\n{n}\t{n}")
        return 0
    else:
        s = sRec2(n - 1) + n
        print(f"{n}\t{s}")
        return s

sRec2(10)