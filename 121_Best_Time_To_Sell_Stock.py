class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprof = 0
        best = prices[0]
        for i in range(1, len(prices)):
            if prices[i]>best:
                maxprof = max(maxprof, prices[i]-best)
            else:
                best = min(best, prices[i])
        return maxprof