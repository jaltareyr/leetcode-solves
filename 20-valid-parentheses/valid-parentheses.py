class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sets = {")": "(", "}": "{", "]":"["}
        stack = []
        for char in s:
            if char in sets.values(): # Opening brackets
                stack.append(char)
            elif char in sets:
                if not stack or stack.pop()!=sets[char]:
                    return False
            else:
                return False
        return not stack

        