class Solution:
    def maxLen(self, arr):
        prefix = 0
        map = {0:-1}
        max_len = 0
        current_len = 0

        for i in range(len(arr)):
            prefix += arr[i]
            if prefix not in map:
                map[prefix] = i
            else:
                current_len = i - map[prefix]
                max_len = max(max_len,current_len)
        return max_len
s = Solution()
a = s.maxLen([6, -2, 2, -8, 1, 7, 4, -10])
print(a)