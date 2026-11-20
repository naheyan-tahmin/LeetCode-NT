# 4 Sum Problem
# Find all the unique quadruplets in the array that sum up to the target
# Time Complexity: O(n^3)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            while j<n:
                p = j+1
                q = n-1
                while p<q:
                    total = nums[i]+nums[j]+nums[p]+nums[q]
                    if total< target:
                        p+=1
                    elif total> target:
                        q-=1
                    else:
                        res.append([nums[i],nums[j],nums[p],nums[q]])
                        p+=1
                        q-=1
                        while p<q and nums[p] == nums[p-1]:
                            p+=1
                j+=1
                while j<n and nums[j] == nums[j-1]:
                    j+=1
        return res

        