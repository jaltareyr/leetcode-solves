class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()

        i = 0
        n = len(intervals)
        result = [intervals[0]]
        
        for i in range(1, n):
            prev = result[-1]
            curr = intervals[i]

            if prev[1] >= curr[0]:
                prev[1] = max(prev[1], curr[1])
            else:
                result.append(curr)
        return result
        