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
        total = []
        elem = []
        for key in tally:
            total.append(tally[key])
            elem.append(key)
        ret = []
        for i in range(0,k):
            top = 0
            topel = 0
            for j in range(len(total)):
                if total[j] > top and elem[j] not in ret:
                    top = total[j]
                    topel = elem[j]
            ret.append(topel)
        return ret

        