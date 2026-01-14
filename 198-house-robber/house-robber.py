class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        robbed = {}
        def torob(i, t):
            if i >= len(nums):
                return t
            if (i,t) in robbed:
                return robbed[(i, t)]
            roby = torob(i+2, t+nums[i])
            
            robn = torob(i+1, t) 
            robbed[(i, t)] = max(roby, robn)
            return max(roby, robn)
        return torob(0, 0)