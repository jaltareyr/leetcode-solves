class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        mp = {"2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        output = [""]
        for digit in digits:
            temp = []
            for ch in mp[digit]:
                for o in output:
                    temp.append(o + ch)
            output = temp
        return output


        

        