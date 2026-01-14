class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = {}
        def torob(n, h):
            rety = 0
            retn = 0
            
            if n >= len(nums):
                return 0
            if (n,h) in v:
                return v[(n,h)]

            if n == len(nums)-1:
                if h:
                    v[(n,h)] = 0
                    return 0
                else:
                    v[(n,h)] = nums[n]
                    return nums[n]
            if n == 0:
                rety = torob(n+2, h=True)
                retn = torob(n+1, h=False)
            else:
                rety = torob(n+2, h)
                retn = torob(n+1, h)
            v[(n,h)] = max(rety+nums[n], retn)
            return v[(n,h)]

        return torob(0,False)