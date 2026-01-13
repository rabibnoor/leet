class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        i = 0

        while(True):
            if i >= len(numbers):
                break
            ntarget = target - numbers[i]
            for j in range(i+1, len(numbers)):
                if ntarget == numbers[j]:
                    return [i+1, j+1]
                if  numbers[j] == numbers[i]:
                    i = j
            i+=1
        return ret

