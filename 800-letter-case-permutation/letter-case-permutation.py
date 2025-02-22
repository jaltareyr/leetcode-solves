class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, temp, start):
            if len(temp) == len_max:
                result.append(''.join(temp[:]))
                return
            for i in range(start, len(s)):
                if s[i].isdigit():
                    dfs(s, temp + [s[i]], i + 1)
                else:
                    dfs(s, temp + [s[i].lower()], i + 1)
                    dfs(s, temp + [s[i].upper()], i + 1)
        
        result = []
        len_max = len(s)
        dfs(s, [], 0)
        return result