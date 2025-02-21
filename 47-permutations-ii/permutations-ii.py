class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    
        def dfs(temp, used):
            if len(temp) == length:
                result.append(list(temp))
                return
            
            for i in range(0, length):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                temp.append(nums[i]) 
                dfs(temp, used)
                temp.pop()
                used[i] = False
        
        nums.sort()
        length = len(nums)
        result = []
        used = [False] * length
        dfs([], used)
        return result