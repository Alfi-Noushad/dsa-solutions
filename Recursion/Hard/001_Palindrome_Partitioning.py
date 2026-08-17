class Solution:
    def partition(self, s: str):

        ans = []

        def isPalindrome(text):
            return text == text[::-1]

        def solve(index,current_list):
            if index == len(s):
                ans.append(current_list[:])
                return
            
            for i in range(index,len(s)):
                if not isPalindrome(s[index:i+1]):
                    continue

                current_list.append(s[index:i+1])
                solve(i+1,current_list)

                current_list.pop()

        solve(0,[])
        return ans
s = Solution()
a = s.partition("aab")
print(a)