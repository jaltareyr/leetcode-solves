class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        m, n = len(word1), len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for row in range(m+1):
            dp[row][0] = row
        for col in range(n+1):
            dp[0][col] = col
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        print(dp)
        return dp[m][n]