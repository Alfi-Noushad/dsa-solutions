class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s) - 1):
            current = roman[s[i]]
            next = roman[s[i + 1]]
            if current >= next:
                value =  current
                result += value
            else:
                value = current
                result -= value
        return result+roman[s[-1]]
s =Solution()
a =s.romanToInt("MCMIV")
print(a)