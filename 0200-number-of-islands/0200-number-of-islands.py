class Solution:
    def getAllConnected(self, grid: List[List[str]], i, j, se, direction):
        if (i, j) in se or grid[i][j] == '0':
            return
        
        se.add((i, j))
        if direction != 'u' and i > 0:
            self.getAllConnected(grid, i-1, j, se, 'd')

        if direction != 'r' and j < len(grid[0]) - 1:
            self.getAllConnected(grid, i, j+1, se, 'l')

        if direction != 'd' and i < len(grid) - 1:
            self.getAllConnected(grid, i+1, j, se, 'u')

        if direction != 'l' and j > 0:
            self.getAllConnected(grid, i, j-1, se, 'r')

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        se = set()
        noOfIslands = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if (i, j) in se or grid[i][j] == '0':
                    continue
                else:
                    noOfIslands += 1
                    self.getAllConnected(grid, i, j, se, 'z')
        
        return noOfIslands