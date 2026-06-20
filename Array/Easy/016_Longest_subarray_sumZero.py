class Solution:
    def longestSubarray(self, arr):
       prefix_sum = 0
       mp = {}
       maxlen = 0

       for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == 0:
                maxlen = max(maxlen, i + 1)
            else:
                if prefix_sum in mp:
                    length = i - mp[prefix_sum]
                    maxlen = max(maxlen, length)
                else:
                    mp[prefix_sum] = i
        

       print(maxlen)

s = Solution()
s.longestSubarray([9, -3, 3, -1, 6, -5])