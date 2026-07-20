l1 = int(input())
a1 = list(map(int, input().split()))
l2 = int(input())
a2 = list(map(int, input().split()))
m = n = 0
op =[]
while(m < l1 and n < l2):
    if(a1[m] > a2[n]):
        op.append(a2[n])
        n = n+1
    elif(a1[m] < a2[n]):
        op.append(a1[m])
        m = m+1
    elif(a1[m] == a2[n]):
        op.append(a2[n])
        n = n+1  
        op.append(a1[m])
        m = m+1
while(m < l1):
    op.append(a1[m])
    m = m+1
while(n < l2):  
    op.append(a2[n])
    n = n+1      
print(*op)                  
        
