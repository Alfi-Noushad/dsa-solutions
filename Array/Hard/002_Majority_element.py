class Solution:
    def majorityElementTwo(self, nums):
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for i in map:
            if map[i] > len(nums)//3:
                print(i)
s= Solution()
s.majorityElementTwo([1, 2, 1, 1, 3, 2])