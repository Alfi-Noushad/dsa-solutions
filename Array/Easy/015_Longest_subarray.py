class Solution:
    def longestSubarray(self, arr, k):
        current_sum = arr[0]
        maxlen = 0
        l = r = 0
        n = len(arr)

        while r < n:

            r += 1
            if r < n:
                current_sum += arr[r]
            
            while l<r and current_sum > k:
                current_sum -= arr[l]
                l += 1
            
            if current_sum == k:
                lenght = r - l + 1
                if maxlen < lenght:
                    maxlen = lenght
        

        print(maxlen)

s = Solution()
s.longestSubarray( [10, 5, 2, 7, 1, 9],15)