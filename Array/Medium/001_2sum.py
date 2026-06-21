class Solution:
    def twoSum(self, arr, target):
        map = {}
        for i in range(len(arr)):
            search = target - arr[i]
            if search in map:
                return [map[search],i]
            else:
                map[arr[i]] = i
                    
s = Solution()
a = s.twoSum([2,6,5,8,11],14)
print(a)
        



"""
class Solution:
    def twoSum(self, arr, target):

        for i in range(len(arr)):
            r = i+1
            
            while r < len(arr):
                if arr[i] + arr[r] != target:
                        r += 1
                else:
                     return i,r
                    
s = Solution()
a = s.twoSum([2,6,5,8,11],14)
print(a)
"""
        