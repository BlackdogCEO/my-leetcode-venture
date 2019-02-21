class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit = 0
        for i in range(len(prices) - 1):
            prices[i] = prices[i + 1] - prices[i]
            if prices[i] > 0:
                profit = profit + prices[i]
        return profit


"""
Runtime: 44 ms, faster than 85.38% of Python3 online submissions for Best Time to Buy and Sell Stock II.
in fact this answer means you can seize every rise in stock price and avoid every loss(decrease).
"""