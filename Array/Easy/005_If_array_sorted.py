class Solution:
    def isSorted(self, arr):
        flag = 0
        for i in range(len(arr)-1):
            if arr[i] <= arr[i+1]:
                flag += 1
            else:
                flag -= 1
        if flag > 0:
            print("sorted")
        else:
            print("Nor sorted")

s = Solution()
s.isSorted([1, 2, 3, 4, 5])


#or

"""
if arr[i] > arr[i+1]:
    print(not sorted)
    return

"""