def binarygcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    shift = 0
    while a % 2 == 0 and b % 2 == 0:
        a //= 2
        b //= 2
        shift += 1
    while a % 2 == 0:
        a //= 2
    while b != 0:
        while b % 2 == 0:
            b //= 2
        if a > b:
            a, b = b, a
        b = b - a
    return a * (2 ** shift)
a, b = map(int, input().split())
print(binarygcd(a, b))            
          
