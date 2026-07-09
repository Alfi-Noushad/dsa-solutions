class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        first = strs[0]
        for i in range(len(first)):
            ch = first[i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return result

            result += ch

        return result
s = Solution()
a = s.longestCommonPrefix(["apple", "banana", "grape", "mango"])
print(a)