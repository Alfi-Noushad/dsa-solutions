class Solution:
    def isPalindrome(self, n):
        org = n
        rev = 0
        while n>0:
            r = n%10
            rev = rev*10 +r
            n = n//10
        if rev == org:
            print(f"The no:{org} palindrome is {rev}")
        else:
            print("Not palindrome")

s = Solution()
s.isPalindrome(121)

#TC: O(log n)
#SP: O(1)