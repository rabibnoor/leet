class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        tally = {}
        for i in nums:
            if i in tally:
                tally[i] += 1
            else:
                tally[i] = 1
        total = [[] for _ in range(len(nums) + 1)]
         
        for key in tally:
            total[tally[key]].append(key)
        ret = []
        for i in range(len(total)-1, 0, -1):
            for v in total[i]:
                ret.append(v)
                if len(ret) == k:
                    return ret




        