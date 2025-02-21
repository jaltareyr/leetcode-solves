class Solution(object):
    def RLE(self, s):
        if not s:
            return ""
        count = 1
        result = "" 
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result += str(count) + str(s[i - 1])
                count = 1
        result += str(count) + str(s[-1])  # Fix: Ensure the last character is added
        
        return result

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """  

        if n == 1:
            return "1"

        result = "1"

        for _ in range(n - 1):
            result = self.RLE(result)
        
        return result


        