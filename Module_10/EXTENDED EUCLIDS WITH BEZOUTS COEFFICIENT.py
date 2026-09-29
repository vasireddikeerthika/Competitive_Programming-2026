def extended_gcd(a, b):
    s1, s2, t1, t2 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        t1, t2 = t2, t1 - q * t2
        s1, s2 = s2, s1 - q * s2
    return s1,t1,a
a,b = map(int,input().split())
print(*extended_gcd(a,b))    
