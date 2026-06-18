class Solution:
    def secondLargestElement(self, arr):
        largest = arr[0]
        secondlargest = -1
        for i in range(len(arr)):
            if arr[i] > largest:
                secondlargest = largest
                largest = arr[i]

            elif arr[i] > secondlargest and arr[i] != largest:
                 secondlargest = arr[i]
        
        print(secondlargest)

s = Solution()
s.secondLargestElement([3, 3, 6, 1])

#tc O(n)
#sp O(1)
