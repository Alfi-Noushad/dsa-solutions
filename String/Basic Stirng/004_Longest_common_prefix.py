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
            for j in range(1,len(strs)):
                if ch[i] == strs[j][i] and ch[i] == strs[j+1][i]:
                    result += ch[i]
                else:
                    return result
s = Solution()
a = s.longestCommonPrefix(["flower", "flow", "flight"])
print(a)