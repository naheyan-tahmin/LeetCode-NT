class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1]*len(nums)
        for i in range(1,len(nums)):
            answer[i]*= nums[i-1]*answer[i-1]
        suffix = 1
        for j in range(len(nums)-2,-1, -1):
            suffix*= nums[j+1]
            answer[j]*=suffix
        return answer
            
        