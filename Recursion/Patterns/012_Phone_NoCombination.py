class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans = []

        def solve(index,current):
            if index == len(digits):
                ans.append(current)
                return
            
            for ch in mapping[digits[index]]:
                solve(index+1,current + ch)

        solve(0,"")
    
        return ans
        