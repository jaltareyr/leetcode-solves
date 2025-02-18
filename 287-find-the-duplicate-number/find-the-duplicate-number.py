class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mymap = {}

        for i  in nums:
            if i in mymap:
                return i
            else:
                mymap[i] = 1
        