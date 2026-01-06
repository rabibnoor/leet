class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ts = {}

        for i, v in enumerate(nums):
            ts[target - v] = i

        for i, v in enumerate(nums):
            if v in ts and ts[v]!=i:
                return[i, ts[v]]
        return []
        