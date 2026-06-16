class Solution:
    def mostFrequentElement(self, nums):
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        print(max(freq.items(),key=lambda x: x[1]))


s = Solution()
s.mostFrequentElement(nums=[1,2,2,1,3,2])