class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        has = {}
        for n in nums:
            if n in has:
                return True
            has[n] = True
        return False