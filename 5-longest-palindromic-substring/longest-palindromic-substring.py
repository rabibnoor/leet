class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ml = -1
        longest = ""
        
        for i in range(len(s)):
            j = k = i
            
            while(j>=0 and k < len(s)):
                if s[j] == s[k]:
                    
                    if (k - j) > ml:
                        ml = k -j
                        longest = s[j:k+1]
                    j -= 1
                    k += 1
                else:
                    break
            j  = i
            k = i+1
            while(j>=0 and k < len(s)):
                if s[j] == s[k]:
                  
                    if (k - j) > ml:
                        ml = k -j
                        longest = s[j:k+1]
                    j -= 1
                    k += 1
                else:
                    break

        return longest