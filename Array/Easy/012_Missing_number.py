"""
class Solution:
    def missingNumber(self, arr):
        sum_t = 0
        sum_e = 0
        sum_ts = 0
        for i in arr:
            sum_t += i
        for i in range(1,len(arr)+2):
            sum_e += i

        sum_ts = sum_e - sum_t

        print(sum_ts)
        

s = Solution()
s.missingNumber([1,2,4,5])
"""
#_________________________________

class Solution:
    def missingNumber(self, arr):
        a = 0
        b = 0
        for i in range(1,len(arr)+2):
            a ^= i
        for i in arr:
            b ^= i
        c = a ^ b

        print(c)
        

s = Solution()
s.missingNumber([1,2,4,5])