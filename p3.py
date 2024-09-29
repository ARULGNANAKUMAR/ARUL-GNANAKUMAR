def max_of_minimums(arr, k):
    n = len(arr)
    max_min = float('-inf')  
    
    
    for i in range(n - k + 1):
        
        current_min = min(arr[i:i+k])
        
        if current_min > max_min:
            max_min = current_min
    
    return max_min


x = int(input()) 
n = int(input())  
space = [int(input()) for _ in range(n)]  


print(max_of_minimums(space, x))
