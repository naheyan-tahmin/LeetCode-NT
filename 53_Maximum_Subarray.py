class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        cs = 0
        ms = float('-inf')
        for i in range(len(nums)):
            cs+=nums[i]
            ms = max(ms,cs)
            if cs<0:
                cs = 0
        return ms