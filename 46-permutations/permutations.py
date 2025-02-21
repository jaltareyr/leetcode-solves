class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def helper(nums, temp):
            if len(temp) == length:
                result.append(list(temp))
                return
            
            for i in range(0, len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                helper(nums, temp)
                temp.pop()
        
        length = len(nums)
        result = []
        helper(nums, [])
        return result