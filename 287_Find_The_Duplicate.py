class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        st = [0]*len(nums)
        for i in nums:
            if st[i] == 1:
               return i
            st[i] = 1
        
        