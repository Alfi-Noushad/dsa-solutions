class Solution:
    """
    def reverse(self, arr: list, n: int):
        rev = arr[::-1]
        print(rev)
        """
    def reverse(self, arr: list, n: int):
        left = 0
        right = len(arr)-1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        print(arr)

s=Solution()
s.reverse([1,2,3,4,5],5)







