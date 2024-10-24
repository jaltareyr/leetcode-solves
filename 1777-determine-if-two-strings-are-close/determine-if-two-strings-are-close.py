class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        flag1 = False
        flag2 = False

        print(set(list(word1)), set(list(word2)))

        if set(list(word1)) ==set(list(word2)):
            flag1 = True
        
        dict1 = {}
        dict2 = {}
        for ch in word1:
            if ch in dict1:
                dict1[ch]+=1
            else:
                dict1[ch]=1

        for ch in word2:
            if ch in dict2:
                dict2[ch]+=1
            else:
                dict2[ch]=1

        print(dict1)
        print(dict2)
        
        if sorted(dict1.values())==sorted(dict2.values()):
            flag2=True
        
        if flag1 and flag2:
            return True
        else:
            return False