class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        n=len(prices)
        minimum=prices[0]
        for i in range(n):
            cost=prices[i]-minimum
            maxprofit=max(maxprofit,cost)
            minimum=min(minimum,prices[i])
        return maxprofit