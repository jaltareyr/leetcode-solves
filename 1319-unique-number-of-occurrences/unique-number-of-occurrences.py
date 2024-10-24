class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        
        hash_map = Counter(arr).values()
        print(hash_map)
        for i, n in enumerate(hash_map):
            if n in hash_map[:i] or n in hash_map[i+1:]:
                return False
        return True
        
        