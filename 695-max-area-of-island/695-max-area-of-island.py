class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        max_region = 0
        
        def mark_current_island(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 0
            
            if grid[row][col] == 0 or grid[row][col] == 2:
                return 0
            
            grid[row][col] = 2
            
            down = mark_current_island(row + 1, col)
            top = mark_current_island(row - 1, col)
            right = mark_current_island(row, col + 1)
            left = mark_current_island(row, col - 1)    
            return top + down + right + left + 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_size = mark_current_island(r, c)
                    max_region = max(max_region, curr_size)       
        return max_region