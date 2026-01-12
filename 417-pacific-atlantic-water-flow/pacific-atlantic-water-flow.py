class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        vis = {}
        rowlim = len(heights)
        collim = len(heights[0])
        moves = [[0, 1],[1, 0], [0, -1], [-1, 0]] 
        ret = []
        def ffil(r, c, p):

           

            h = heights[r][c]
            if p:
                if r in vis:
                    if c in vis[r]:
                        return
                    else: 
                        vis[r][c] = 1
                else:
                    vis[r] = {}
                    vis[r][c] = 1
            else:
                if r in vis:
                    if c in vis[r]:
                        if  vis[r][c] == 1:
                            vis[r][c] = 2
                            ret.append([r,c])
                        elif vis[r][c] == 2:
                            return
                    else: 
                        vis[r][c] = 2
                else:
                    vis[r] = {}
                    vis[r][c] = 2
                


            for m in moves:
                nr = r+m[0]
                nc = c+m[1]
                if not(nr < 0 or nr >= rowlim or nc < 0 or nc>= collim):
                    if heights[nr][nc] >= h:
                        ffil(nr,nc, p)
        
        for i in range (collim):
            ffil(0,i, True)
        
        for i in range (0, rowlim):
            ffil(i,0, True)

        for i in range (collim):
            ffil(rowlim-1, i, False)
        
        for i in range (0, rowlim):
            ffil(i,collim-1, False)
        return ret