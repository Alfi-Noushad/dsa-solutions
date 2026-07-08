class Solution(object):
    def reverseWords(self, s):
        result = []
        i = len(s) - 1

        while i >= 0:
            # Skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1

            if i < 0:
                break

            # Find the beginning of the word
            j = i
            while j >= 0 and s[j] != " ":
                j -= 1

            result.append(s[j+1:i+1])

            i = j

        return " ".join(result)


sol = Solution()
print(sol.reverseWords("hello world"))      
