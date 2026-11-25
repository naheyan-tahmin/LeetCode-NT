class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        st = 0
        end = n-1

        while st < m  and end >= 0:
            if target == matrix[st][end]:
                return True
            elif target<matrix[st][end]:
                end-=1
            else:
                st+=1
        return False

        