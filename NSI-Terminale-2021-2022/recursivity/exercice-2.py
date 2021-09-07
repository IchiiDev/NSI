def sRec1(n):
    if n == 0:
        return 0
    else:
        return sRec1(n - 1) + n


sRec1(3)