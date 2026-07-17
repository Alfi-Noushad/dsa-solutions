class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = {}
        ss = ""
        for ch in s:
            if ch not in map:
                map[ch] = 1
            else:
                map[ch] += 1
        
        sa = sorted(map.items(), key=lambda x: x[1], reverse=True)
        for ch,count in sa:
            k = ch * count
            ss += k
        return ss
s = Solution()
a= s.frequencySort("tree")
print(a)