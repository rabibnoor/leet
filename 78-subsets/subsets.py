class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []    
        subset = []

        def dfs(i):
            if i >= len(nums):
                ret.append(list(subset))
                return 
            
            #pick
            subset.append(nums[i])
            dfs(i+1)

            #dontpick
            subset.pop()
            dfs(i+1)
        dfs(0)
        return ret
        






        