def maxSubarray(arr):
    max_sofar = arr[0]
    max_end = 0
    for i in range(0,len(arr)):
        max_end = max_end + arr[i]
        if max_sofar < max_end:
            max_sofar = max_end
        if max_end < 0:
            max_end = 0
    return max_sofar       
                  
l = int(input())
arr = list(map(int, input().split()))    
print(maxSubarray(arr))    
        
