class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        if set(word1) != set(word2):
            return False
        
        dict1 = Counter(word1)
        dict2 = Counter(word2)
        
        return Counter(dict1.values()) == Counter(dict2.values())