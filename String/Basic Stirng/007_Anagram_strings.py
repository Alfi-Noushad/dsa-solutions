class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq = {}
        if len(s) != len(t):
            return False
        else:
            for ch in s:
                if ch not in freq:
                    freq[ch] = 1
                else:
                    freq[ch] += 1
            for ch in t:
                if ch in freq:
                    freq[ch] -= 1
                else:
                    return False
            for value in freq.values():
                if value != 0:
                 return False

        return True
            
s = Solution()
a = s.isAnagram("bat","rat")
print(a)