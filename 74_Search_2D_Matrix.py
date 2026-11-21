# 74. Search a 2D Matrix by Binary Search Method, Time Complexity: O(log(r*c)), Space Complexity: O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        c = len(matrix[0])
        st = 0
        end = r-1
        while st<=end:
            mid = st + (end-st)/2
            if target>=matrix[mid][0] and target<=matrix[mid][c-1]:
                strt = 0
                en = c-1
                while strt<=en:
                    middle = strt+(en-strt)/2
                    if target == matrix[mid][middle]:
                        return True
                    elif target < matrix[mid][middle]:
                        en = middle - 1
                    else:
                        strt = middle + 1
                return False
            elif target<matrix[mid][0]:
                end = mid - 1
            else:
                st = mid + 1
        return False