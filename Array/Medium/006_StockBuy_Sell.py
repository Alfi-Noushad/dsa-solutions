class Solution:
    def stockBuySell(self, arr):
        lowest_val = arr[0]
        max_profit = 0
        profit = 0
        for i in range(1,len(arr)):
            profit = arr[i] - lowest_val 
            max_profit = max(max_profit,profit)
            if lowest_val >= arr[i]:
                lowest_val = arr[i]
            
        return max_profit

s = Solution()
a = s.stockBuySell([7,1,5,3,6,4])
print(a)
            