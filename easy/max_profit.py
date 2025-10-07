from typing import List
def maxProfit(prices: List[int]) -> int:
    if len(prices) == 1:
        return 0
    
    max_profit = 0
    curr_max_profit = 0
    buy = prices[0]

    for i in range(1, len(prices)):
        if prices[i] > buy:
            curr_max_profit = prices[i] - buy
            max_profit = max(max_profit, curr_max_profit)
        
        #buy if price is lower
        if prices[i] < buy:
            buy = prices[i]

    return max_profit

prices = [7,1,5,3,6,4]

print(maxProfit(prices))