#31. Next Permutation 
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        piv = -1
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                piv = i
                break
        if piv == -1:
            
            return nums.reverse()

        for i in range(n-1,piv,-1):
            if nums[piv]<nums[i]:
                temp = nums[piv]
                nums[piv] = nums[i]
                nums[i] = temp
                break
        nums[piv+1:]= reversed(nums[piv+1:])
        return nums

        
        
        