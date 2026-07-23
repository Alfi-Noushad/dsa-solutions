class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""

        l = len(s)
        i = l-1
        while i >=0:
            while i>=0 and s[i] == " ":
                i -= 1
            end = i

            if i<0:
                break

            while i>=0 and s[i] != " ":
                i -= 1

            word = s[i+1:end+1]

            if result != "":
                result += " "

            result += word

        return result


sol = Solution()
print(sol.reverseWords("hello world"))



'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        return " ".join(words)



sol = Solution()
print(sol.reverseWords("hello world"))

'''