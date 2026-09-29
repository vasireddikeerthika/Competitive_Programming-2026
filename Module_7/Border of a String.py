n = input()
op = ""
i=0
j=len(n)-1
if len(set(n)) == 1:
    print(n[:-1])
else:
    while i<=j:
        if n[i] == n[j]:
            op = op + n[i]
            i = i+1
            j = j-1
        else:  
            break  
print(op)
