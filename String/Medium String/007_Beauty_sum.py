class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for i in range(len(s)):
            freq = {}

            for j in range(i, len(s)):
                if s[j] not in freq:
                    freq[s[j]] = 1
                else:
                    freq[s[j]] += 1
                maxm = max(freq.values())
                minm = min(freq.values())
                ans += maxm - minm

        return ans 
s = Solution()
a = s.beautySum("xyx")
print(a)