class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sd = {}
        if len(s)!=len(t):
            return False
        if len(s) == 0:
            return True

        for i in s:
            if i in sd:
                sd[i]+=1
            else:
                sd[i] = 1
        for i in t:
            if i in sd:
                sd[i]-=1
            else:
                return False
        for i in sd:
            if sd[i] != 0:
                return False

        return True

        