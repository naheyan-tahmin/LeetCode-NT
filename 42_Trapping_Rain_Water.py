# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        ans = 0
        l = 0
        r = n-1
        lmax = 0
        rmax = 0
        while l<r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if lmax<rmax:
                ans+= lmax-height[l]
                l+=1
            else:
                ans+= rmax-height[r]
                r-=1
        return ans
        