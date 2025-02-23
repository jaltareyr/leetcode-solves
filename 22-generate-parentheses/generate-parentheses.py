class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(temp, count_open, count_close):
            if len(temp) == 2 * n:
                result.append("".join(list(temp)))
                return
            
            if count_open < n:
                temp.append("(")
                dfs(temp, count_open + 1, count_close)
                temp.pop()
            if count_close < count_open:
                temp.append(")")
                dfs(temp, count_open, count_close + 1)
                temp.pop()

        result = []
        dfs([], 0, 0)
        return result