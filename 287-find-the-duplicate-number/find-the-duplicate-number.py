class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mymap = set()

        for i  in nums:
            if i in mymap:
                return i
            else:
                mymap.add(i)
        