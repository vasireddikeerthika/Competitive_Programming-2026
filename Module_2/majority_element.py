n = int(input())
arr = list(map(int,input().split()))
ref = list(set(arr))
max_count = 0
count = 0
max_el = ref[0]
for i in range(len(ref)):
    count = 0
    for j in range(n):
        if ref[i] == arr[j]:
            count = count+1
    if count > max_count:
        max_count = count 
        max_el = ref[i]
if max_count > n/2 :
    print(max_el)
else:
    print(-1)            
               
            
            
