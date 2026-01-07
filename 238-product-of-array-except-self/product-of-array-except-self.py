class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        mul = 1
        prefix = []
        for i in nums:
            mul = i*mul
            prefix.append(mul)
        
        mul = 1
        suffix = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            mul *= nums[i]
            suffix[i] = mul
        ret = []
        for i in range(len(nums)):
            pre = 1
            suf = 1
            if i - 1 >= 0:
                pre = prefix[i-1]
            
            if i +1 < len(nums):
                suf = suffix[i+1]
            ret.append(pre*suf)

        return ret
            




        