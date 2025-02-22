class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(temp, start):
            result.append(list(temp))
            
            for i in range(start, max_length):
                dfs(temp + [nums[i]], i + 1)
        
        result = []
        max_length = len(nums)
        dfs([], 0)
        return result
        