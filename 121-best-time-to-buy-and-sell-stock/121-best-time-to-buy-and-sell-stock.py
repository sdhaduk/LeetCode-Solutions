class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxP = 0
        
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxP = max(profit, maxP)
            else:
                buy = sell
            sell += 1
            
        return maxP
            
            
            
            
        
        
            
            
            