class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sets = {
            "(": ")", "{": "}", "[":"]"
        }
        stack = []
        for char in s:
            if char in sets.keys():
                stack.append(char)
            else:
                if stack:
                    if char==sets[stack[-1]]:
                        stack.pop()
                    else:
                        return False                        
                else:
                    return False
        
        if stack:
            return False
        else:
            return True

        