class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rl = len(grid)
        cl = len(grid[0])
        moves = [[0, 1],[1, 0], [0, -1], [-1, 0]] 
        def ffil(r, c):
            if r < 0 or r >= rl or c < 0 or c>= cl:
                return
            if grid[r][c] == "0" :
                return
            grid[r][c] = "0"
            for m in moves:
                ffil(r+m[0],c+m[1])

        count = 0
        for i in range(rl):
            for j in range(cl):
                if grid[i][j]  == "1":
                    ffil(i, j)
                    count+=1
        return count
            
            