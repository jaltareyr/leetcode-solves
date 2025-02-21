class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r>= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] ='0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands+=1
        return islands