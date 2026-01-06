class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        srt = []
        for i in range(0, 26):
            #print(i, chr(ord('a') + i))
            srt.append(0)  
        words = {}
        for st in strs:
            for i in range(0, 26):
                srt[i] = 0
            for c in st:
                chv = ord(c)-ord('a')
                srt[chv]+=1
            val = ""
            for i in range(0, 26):
                if srt[i]!=0:
                    val += str(i) + "@" + str(srt[i]) +"$"
                    srt[i] = 0
            if val in words: 
                words[val].append(st) 
            else: 
                words[val] = [] 
                words[val].append(st) 
        ret = [] 
        for k in words: 
            ret.append(words[k]) 
        return ret
            
            