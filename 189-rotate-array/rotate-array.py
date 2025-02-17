class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        def reverse(l, start, end):
            i = start
            j = end-1
            
            while i<j:
                l[i], l[j] = l[j], l[i]
                i+=1
                j-=1
            return l

        n = len(nums)
        k%=len(nums,)

        reverse(nums, 0, n)
        print(nums)

        reverse(nums, 0, k)
        print(nums)

        reverse(nums, k, len(nums))
        print(nums)
            
