class Solution:
    def countFrequencies(self, nums):
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        
        print(freq)
    


s = Solution()
s.countFrequencies(nums=[1,2,2,1,3])

#Time Complexity: O(n)
#Space Complexity: O(n)