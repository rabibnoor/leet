class Solution(object):
    
    dpstep = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb(n):
            if n <=2:
                return n
            if n in self.dpstep:
                return self.dpstep[n]
            step1 = climb(n-1)
            step2 = climb(n-2)
            self.dpstep[n] = step1 + step2
            return step1 + step2
        return climb(n)