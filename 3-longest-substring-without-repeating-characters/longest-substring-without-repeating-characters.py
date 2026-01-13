class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 1
        vis = {}
        if not s:
            return 0
        vis[s[0]] = True
        longest = 1
        while(i<len(s) and j < len(s)):
            if s[j] in vis and vis[s[j]]:
                while(i<j):
                    if s[i] == s[j]:
                        i += 1
                        break
                    vis[s[i]] =False
                    i+=1
                #print(i,s[i], j+1)
            if j - i + 1> longest:
                longest =  j - i + 1
            vis[s[j]] = True
            j+=1
        return longest
        
            

            
        