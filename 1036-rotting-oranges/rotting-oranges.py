class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rl = len(grid)
        cl = len(grid[0])
        moves = [[0, 1],[1, 0], [0, -1], [-1, 0]] 
     
        def ffil(r, c, d):

            if r < 0 or r >= rl or c < 0 or c>= cl:
                return
            if grid[r][c] != 1:
                if grid[r][c] == 0:
                    return
                if  grid[r][c] < d:
                    return
                if grid[r][c] == 2:
                    d = 2

            grid[r][c] = d

            for m in moves:
                ffil(r+m[0],c+m[1], d+1)
            return d
       
        for i in range(rl):
            for j in range(cl):
                if grid[i][j]  == 2:
                    ffil(i, j, 0)
        mx = 0
        #print(grid)
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 1:
                    return -1
              
                if grid[i][j] > mx:
                    mx = grid[i][j]
        if mx == 0:
            return 0
        return mx - 2
        