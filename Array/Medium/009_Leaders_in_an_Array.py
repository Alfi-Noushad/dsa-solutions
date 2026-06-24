class Solution:
    def leaders(self, arr):
        max_right = arr[-1]
        leaders = []
        for i in range(len(arr)-1,-1,-1):
            if max_right <= arr[i]:
                leaders.append(arr[i])
                max_right = arr[i]
        leaders.reverse()
        return leaders
s = Solution()
a = s.leaders([10, 22, 12, 3, 0, 6])
print(a)
           

        