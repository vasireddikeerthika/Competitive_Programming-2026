import math
def gcd(a,b):
    if b == 0:
        return a 
    return gcd(b,a%b)            
a,b,t = map(int,input().split())
x = gcd(a,b)
if t <= max(a,b) and t % x == 0:
    print("YES")
else:
    print("NO")
