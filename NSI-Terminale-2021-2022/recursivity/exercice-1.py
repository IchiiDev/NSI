def slte1(n):
    s = 0
    for i in range(n):
        s = s + n
    return s

def slte2(n):
    s = 0
    print(f"n\ts\n{n}\t{s}")
    for i in range(n):
        s = s + n
        print(f"{n}\t{s}")

slte2(13)