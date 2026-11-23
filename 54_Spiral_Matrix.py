#TC: O(m*n)
#SC: O(1)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        col = len(matrix[0])
        st_r = 0
        st_c = 0
        end_r = row-1
        end_c = col-1
        ans = []

        while st_r <= end_r and st_c <= end_c:
           #top
            for j in range(st_c,end_c+1,1):
                ans.append(matrix[st_r][j])

            #right
            for i in range(st_r+1, end_r+1,1):
                ans.append(matrix[i][end_c])

            #bottom
            for j in range(end_c-1, st_c-1,-1):
                if st_r == end_r:
                  break
                ans.append(matrix[end_r][j])

            #left   
            for i in range(end_r-1,st_r,-1):
                if st_c == end_c:
                    break
                ans.append(matrix[i][st_c])
            
            st_r+= 1
            st_c+=1
            end_r-=1
            end_c-=1
        
        return ans
             

        