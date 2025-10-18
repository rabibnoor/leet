class Trie(object):

    def __init__(self):
        self.myTrie = {}
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if word:
            word += "$"
            trie = self.myTrie
            for i in word:
                if i in trie:
                    trie = trie[i]
                else:
                    trie[i] = {}
                    trie = trie[i]
            #print(self.myTrie)


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word:
            word += "$"
            return self.startsWith(word)

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        word = prefix
        if word:
            trie = self.myTrie
            for i in word:
                if i in trie:
                    trie = trie[i]
                else:
                    return False
            return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)