n = int(input())
s = input().split(',')
ptr = input()
found = False
for i in s:
    cap = ''
    for j in i:
        if j.isupper():
            cap += j
    if ptr in cap:
        print(i) 
        found = True
if not found:
    print("No match found")                  
