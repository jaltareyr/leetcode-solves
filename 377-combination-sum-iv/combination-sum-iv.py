class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def backtrack(nums, target):
            if dp[target] > -1:
                return dp[target]
            
            result = 0
            for i in nums:
                if i <= target:   
                    result += backtrack(nums, target - i)
            
            dp[target] = result
            return result
        

        dp = [-1 for i in range(0, target + 1)]
        dp[0] = 1
        backtrack(nums, target)
        print(dp)
        return dp[target]
