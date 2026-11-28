# 3. Longest Substring Without Repeating Characters
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        uniq = set()
        maxLen = 0

        while r < len(s):
            if s[r] not in uniq:
                uniq.add(s[r])
                maxLen = max(maxLen, r-l+1)
                r+=1
            else:
                uniq.remove(s[l])
                l+=1
        return maxLen
        
        