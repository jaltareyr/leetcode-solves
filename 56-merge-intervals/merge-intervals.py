class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()

        i = 0
        n = len(intervals)
        while i < n-1:

            if intervals[i][1] >= intervals[i + 1][0]: # overlap found
                intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1]) 
                intervals.pop(i)
                n = len(intervals)
            else:
                i+=1
        return intervals

        