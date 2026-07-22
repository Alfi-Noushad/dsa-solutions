class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
           
                left = i
                right = i

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1

                if len(s[left + 1:right]) > len(ans):
                    ans = s[left + 1:right]
           
                left = i
                right = i + 1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1

                if len(s[left + 1:right]) > len(ans):
                    ans = s[left + 1:right]

        return ans

s = Solution()
a = s.longestPalindrome("abba")
print(a)
