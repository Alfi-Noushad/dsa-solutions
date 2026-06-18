class Solution:
    def secondsmallestElement(self, arr):
        smallest = arr[0]
        secondsmallest = -1
        for i in range(len(arr)):
            if arr[i] < smallest:
                secondsmallest = smallest
                smallest = arr[i]
            elif arr[i] < secondsmallest and arr[i] != smallest:
                secondsmallest = arr[i]
        
        print(secondsmallest)

s = Solution()
s.secondsmallestElement([3, 3, 6, 1])

#tc O(n)
#sp O(1)
