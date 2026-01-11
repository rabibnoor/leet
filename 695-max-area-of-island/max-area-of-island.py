class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rl = len(grid)
        cl = len(grid[0])
        moves = [[0, 1],[1, 0], [0, -1], [-1, 0]] 
        def ffil(r, c):
            if r < 0 or r >= rl or c < 0 or c>= cl:
                return 0
            if grid[r][c] == 0 :
                return 0
            grid[r][c] = 0
            s = 0
            for m in moves:
                s+= ffil(r+m[0],c+m[1])
            return s+ 1

        count = 0
        for i in range(rl):
            for j in range(cl):
                if grid[i][j]  == 1:
                    c = ffil(i, j)
                    if c > count:
                        count = c
        return count