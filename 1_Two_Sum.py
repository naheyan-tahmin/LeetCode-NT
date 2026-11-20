#1_Two_Sum With nlogn time complexity.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        new = []
        for i in range(len(nums)):
            new.append((nums[i],i))
        new.sort()
        i = 0
        j = len(new)-1
        while i<j:
            result = new[i][0] + new[j][0]
            if result<target:
                i+= 1
            elif result> target:
                j-=1
            else:

                return [new[i][1],new[j][1]]
        