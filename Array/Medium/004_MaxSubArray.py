#Kadane's Algorithm
class Solution:
    def maxSubArray(self, arr):
        sums = 0
        max_sum = arr[0]
        for i in arr:
            sums += i

            max_sum = max(max_sum,sums)

            if sums < 0:
                sums = 0
            
        return max_sum

s = Solution()
a = s.maxSubArray([-2, -3, -7, -2, -10, -4]) 
print(a)



        
