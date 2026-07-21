class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        sign = 1
        while i< len(s) and s[i] == " ":
            i +=1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '+':
                sign = 1
            else:
                sign = -1
            i += 1
        while i<len(s) and s[i].isdigit():
            num = num *10 + int(s[i])
            i +=1
        num *= sign

        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num

s = Solution()
a =s.myAtoi("-4193 with words")
print(a)
        