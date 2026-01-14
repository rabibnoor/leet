class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minm = 1
        maxm = 1
        trumax = max(nums)
        for i in nums:
            if i == 0:
                maxm = 1
                minm = 1
                continue
            premax = maxm
            maxm = max(maxm*i, i, minm*i)
            minm = min(premax*i, i, minm*i)

            if maxm > trumax:
                trumax = maxm
        return trumax


        