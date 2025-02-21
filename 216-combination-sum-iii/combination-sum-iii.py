class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtrack(n, temp, start):
            if len(temp) == k:
                if n == 0:
                    result.append(list(temp))
                return
        
            for i in range(start, 10):
                temp.append(i)
                new = n - i
                if new >= 0 and len(temp) <= k:
                    backtrack(new, temp, i + 1)
                if len(temp) > 0:
                    temp.pop(-1)
        
        result = []
        candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        backtrack( n, [], 1)
        return result