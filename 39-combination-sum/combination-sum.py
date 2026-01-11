class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ret = set()
        subset = []
        can = sorted(candidates)
        hsh = {}
        def dfs(n):
            if n == 0:
                ret.add(tuple(sorted(list(subset))))
                return 
            if n < 0:
                return 
            for i in can:

                subset.append(i)
                dfs(n-i)
                subset.pop()

        dfs(target)
        return [list(t) for t in ret]

            

           
  
                
                

        