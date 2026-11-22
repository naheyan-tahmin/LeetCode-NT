class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = []
        if len(intervals) == 1:
            return intervals
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            a = intervals[i][0]
            b = intervals[i][1]
            if ans[-1][1] >= a:
                ans[-1][1] = max(ans[-1][1],b)
            else:
                ans.append(intervals[i])
            
        return ans
