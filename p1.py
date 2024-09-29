def max_profit(n, prices):
    min_price = float('inf')  
    max_profit = 0            
    for price in prices:    
        if price < min_price:
            min_price = price
        profit = price - min_price 
        if profit > max_profit:
            max_profit = profit
    return max_profit
n = int(input())  
prices = list(map(int, input().split()))  
print(max_profit(n, prices))
