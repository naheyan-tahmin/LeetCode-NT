# 3 Sum Problem
# Find all the unique triplets in the array that sum up to the target
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)-1
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum<0:
                    j+=1
                elif sum>0:
                    k-=1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
        return result
                

        