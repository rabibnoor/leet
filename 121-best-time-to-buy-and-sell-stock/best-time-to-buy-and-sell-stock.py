class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxp = 0
        i = 0
        lenp = len(prices)
        j = i+1

        while(i<lenp and j < lenp):
            p =  prices[j] - prices[i]
            if p > maxp:
                maxp = p
            if prices[j] < prices[i]:
                i = j
            j+=1
        return maxp
            

        
            
            
        