class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output = [""]
        for ch in s:
            temp = []
            for o in output:
                if ch.isdigit():
                    temp.append(o + ch)
                else:
                    temp.append(o + ch.upper())
                    temp.append(o + ch.lower())
            output = temp
        return output