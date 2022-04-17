class Solution:
    def checkValid(self, board: List[List[int]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        
        
        for r in range(len(board)):
            for c in range(len(board)):
                #If element exist in any of the three sets, return False
                if board[r][c] in rows[r] or board[r][c] in cols[c]:
                    return False
                
                #Add element if it doesn't exist
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                
        return True