import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = sys.maxsize
        profit = 0
        for price in prices:
            if(price < minPrice):
                minPrice = price
            else:
                profit = max(profit, price-minPrice)
        return profit
