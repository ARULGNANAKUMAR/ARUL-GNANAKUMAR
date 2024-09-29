def find_odd_balloon(N, B):
    
    freq = {}
    
    
    for balloon in B:
        if balloon in freq:
            freq[balloon] += 1
        else:
            freq[balloon] = 1
    
    
    for balloon in B:
        if freq[balloon] % 2 != 0:
            print(balloon)
            return
    
    
    print("All are even")


N = int(input())  
B = [input().strip() for _ in range(N)]  


find_odd_balloon(N, B)
