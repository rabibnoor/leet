class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lenh = len(height)
        i = 0
        j = lenh - 1
        maxw = 0
        while(i < lenh and j >-1 and i < j):
            w = min(height[i], height[j]) * (j - i)
            if w > maxw:
                maxw = w
            if height[i] < height[j]:
                i +=1
            else:
                j-=1
        return maxw

