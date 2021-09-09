def fac2(n):
    assert type(n) == int
    assert n > 0
    if n == 0 or n == 1:
        print(f"1\t1")
        return 1
    result = fac2(n - 1) * n
    print(f"{n}\t{result}")
    return result

print("n\tn!")
produit = fac2(10)