class Solution:
    def aggressiveCows(self, nums, k):
        nums.sort()
        low = 1
        high = nums[-1] - nums[0]
        

        while low<=high:
            mid = (low+high)//2
            count = 1
            lastPlaced = nums[0]
            for i in range(1,len(nums)):
                if nums[i] - lastPlaced >= mid:
                    count += 1
                    lastPlaced = nums[i]
            
            if count >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

s = Solution()
a = s.aggressiveCows([0,3,4,7,10,9],4)
print(a)

            

