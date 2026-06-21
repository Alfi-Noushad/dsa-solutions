class Solution:
    def majorityElement(self, arr):
        count = 0
        candidate = None

        for num in arr:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1

            else:
                count -= 1

        return candidate


            
s = Solution()
a = s.majorityElement([7, 0, 0, 1, 7, 7, 2, 7, 7])
print(a)



"""

class Solution:
    def majorityElement(self, arr):
        map = {}
        for i in range(len(arr)):
            if arr[i] in map:
                map[arr[i]] += 1
            else:
                map[arr[i]] = 1

            if map[arr[i]] >len(arr) // 2:
                return arr[i]
            
s = Solution()
a = s.majorityElement([7, 0, 0, 1, 7, 7, 2, 7, 7])
print(a)

"""


"""
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        nums.sort()
        return nums[n//2]

"""