def preprocess(s):
    n = len(s)
    
   
    prefix_frogs = [0] * (n + 1)  
    left_stone = [-1] * n         
    right_stone = [-1] * n        
    
    
    last_stone = -1
    for i in range(n):
        if s[i] == '|':
            last_stone = i
        left_stone[i] = last_stone
        prefix_frogs[i + 1] = prefix_frogs[i] + (1 if s[i] == '*' else 0)
    
    
    last_stone = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            last_stone = i
        right_stone[i] = last_stone
    
    return prefix_frogs, left_stone, right_stone

def count_frogs_between_stones(s, startIndex, endIndex):
    
    prefix_frogs, left_stone, right_stone = preprocess(s)
    
    result = []
    
    for start, end in zip(startIndex, endIndex):
        start -= 1  
        end -= 1    
        
        
        left_boundary = right_stone[start]
        
        right_boundary = left_stone[end]
        
        
        if left_boundary != -1 and right_boundary != -1 and left_boundary < right_boundary:
            frogs_between = prefix_frogs[right_boundary + 1] - prefix_frogs[left_boundary + 1]
            result.append(frogs_between)
        else:
            result.append(0)  
    
    return result


s = input() 
n = int(input())  
startIndex = [int(input()) for _ in range(n)]  
endIndex = [int(input()) for _ in range(n)]    


output = count_frogs_between_stones(s, startIndex, endIndex)
for res in output:
    print(res)
