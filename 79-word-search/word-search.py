class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rl = len(board)
        cl = len(board[0])
        vis = {}
        def dfs(r, c, idx):

            if idx > len(word):
                return True
            #print(word[idx], r, c)
            if idx == len(word)-1 and board[r][c] == word[idx]:
                return True
            for i in moves:
                rn = r + i[0]
                cn = c + i[1]
                if rn >= 0 and rn < rl and cn >= 0  and cn < cl:
                    if board[rn][cn] == word[idx+1] and (rn, cn) not in vis:
                        vis[(rn, cn)] = True
                        if dfs(rn, cn, idx + 1):
                            return True
                        del vis[(rn, cn)]
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    vis[(i,j)] = True
                    if dfs(i, j, 0):
                        return True
                    del vis[(i,j)]
        return False
                
                        

            

        