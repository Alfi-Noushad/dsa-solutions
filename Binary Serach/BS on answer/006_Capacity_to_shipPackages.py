class Solution(object):
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)
        

        while low <= high:
            currentLoad = 0
            daysNeeded = 1
            mid = (low+high) // 2
            for weight in weights:
                if currentLoad + weight <= mid:
                    currentLoad += weight
                else:
                    daysNeeded += 1
                    currentLoad = weight
            if daysNeeded <= days:
                high = mid - 1
            else:
                low = mid + 1
            
        return low
    
s = Solution()
a = s.shipWithinDays([5, 4, 5, 2, 3, 4, 5, 6],5)
print(a)
            
            
            
            
                    

        
        