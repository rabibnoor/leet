class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ret = []
        subset = []
        can = sorted(candidates)
        def dfs(i, cur, total):
            if total == target:
                ret.append(list(cur))
                return 
            if i>=len(candidates) or total > target:
                return 
            
            cur.append(can[i])
            dfs(i, cur, total+can[i])
            cur.pop()
            dfs(i+1, cur, total)
            
        dfs(0, subset, 0)
        return ret

            

           
  
                
                

        