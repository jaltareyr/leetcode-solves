class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtrack(candidates, target, temp_result, start):
            if target == 0:
                result.append(list(temp_result))
                return

            for i in range(start, len(candidates)):
                temp_result.append(candidates[i])
                newTarget = target - candidates[i]
                if newTarget >= 0:
                    backtrack(candidates, newTarget, temp_result, i)
                temp_result.pop(-1)
        
        result = []
        candidates.sort()
        backtrack(candidates, target, [], 0)

        return result

