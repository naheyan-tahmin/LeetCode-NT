 #Dutch National Flag Algo
 # Sort 0,1,2 in the array
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid<= high:
            #Dutch National Flag Algo
            if nums[mid] == 0:
                temp = nums[mid]
                nums[mid] = nums[low] 
                nums[low] = temp 
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp
                high-= 1
        return nums 

        