class Solution:    
    def palindromeCheck(self, s):
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                print("Not palindrome")
                return
            left += 1
            right -= 1
        
        print("palindrome")

s = Solution()
s.palindromeCheck("hello")