class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        char_map = {}
        result = 0
        for i, char in enumerate(s):
            
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            else:
                result = max(result, i - start + 1)
            
            char_map[char] = i
            
        return result

