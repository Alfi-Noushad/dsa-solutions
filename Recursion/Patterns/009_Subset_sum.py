class Solution:
    def subsetSums(self, arr):
        ans = []
        def solve(index, current_sum):

            if index == len(arr):
                ans.append(current_sum)
                return
            # Take
            solve(index + 1,current_sum + arr[index])
            # Skp
            solve(index + 1,current_sum)

        solve(0, 0)
        return ans
    
s = Solution()
print(s.subsetSums([1,2,3]))