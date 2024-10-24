class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hash_map = {}
        
        for a in arr:
            if a in hash_map.keys():
                hash_map[a]+=1
            else:
                hash_map[a]=1
        counts = hash_map.values()
        print(counts)
        for i, n in enumerate(counts):
            if n in counts[:i] or n in counts[i+1:]:
                return False
        return True
        
        