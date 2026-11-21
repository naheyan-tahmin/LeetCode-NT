# 11. Container With Most Water by Two Pointers Method.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_a = 0
        i = 0
        j = len(height)-1
        while i<j:
                w = j-i
                h = min(height[i], height[j])
                area = w*h
                max_a = max(max_a,area)
                if height[i]<height[j]:
                    i+= 1
                else:
                    j-= 1
        return max_a
        