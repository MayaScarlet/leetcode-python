class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:        
#         rows = len(matrix)
#         cols = len(matrix[0])
#         max_edge = 0
        
#         for row in range(rows):
#             for col in range(cols):
#                 # calculate max edge
#                 if row == 0 or col == 0:
#                     max_edge = max(max_edge, int(matrix[row][col]))
                    
#                 # if current cell is 1, current cell = min of (top cell, left cell and diagonal left cell) + 1 
#                 elif matrix[row][col] == '1':
#                     matrix[row][col] = min(max_edge, int(matrix[row-1][col-1]),
#                         int(matrix[row-1][col]), int(matrix[row][col-1])) + 1
                
#                     max_edge = max(max_edge, matrix[row][col])
                
#         return max_edge ** 2

        #Time and space complexity: O(m*n)
        rows, cols = len(matrix), len(matrix[0])
        cache = {} # map(row, col) to maxlength of square
        
        def helper(row, col):
            if row >= rows or col >= cols:
                return 0
            
            if (row, col) not in cache:
                down = helper(row + 1, col)
                right = helper(row, col + 1)
                diagonal = helper(row + 1, col + 1)
                
                cache[(row, col)] = 0
                if matrix[row][col] == "1":
                    cache[(row, col)] = 1 + min(down, right, diagonal)
                
            return cache[(row, col)]
        helper(0, 0)
        return max(cache.values()) ** 2
        