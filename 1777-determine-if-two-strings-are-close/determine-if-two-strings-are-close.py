class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        from collections import Counter

        freq1 = Counter(word1)
        freq2 = Counter(word2)
        flg1 = False
        flg2 = False
        if set(freq1.keys()) == set(freq2.keys()):
            flg1 = True
        
        if Counter(freq1.values()) == Counter(freq2.values()):
            flg2 = True

        print(flg1, flg2)
        
        if flg1 and flg2:
            return True
        else:
            return False
        
        