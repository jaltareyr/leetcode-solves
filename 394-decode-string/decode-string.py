class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for letter in s:
            if letter !=']':
                stack.append(letter)
                print("new stack:", ''.join(stack))
            else:
                i = len(stack) - stack[::-1].index('[') - 1
                number = ""
                j = 1
                while len(stack[:i]) >=j and stack[:i][-j].isnumeric():
                    j+=1
                number = int(''.join(stack[:i][-(j-1):]))
                print(stack[:i - j + 1])
                stack = stack[:i - j + 1] + stack[i+1:] * number
        return ''.join(stack)

        