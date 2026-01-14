class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        robbed = {}
        def torob(i):
            if i >= len(nums):
                return 0
            if i in robbed:
                return robbed[i]
            roby = torob(i+2)
            
            robn = torob(i+1) 
            robbed[i] = max(nums[i]+roby, robn)
            return robbed[i] 
        return torob(0)