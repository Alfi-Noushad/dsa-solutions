class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def countPairs(self, arr, low, mid, high):
        count = 0
        right = mid + 1

        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            count += right - (mid + 1)

        return count

    def mergeSort(self, arr, low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2

        count = self.mergeSort(arr, low, mid)
        count += self.mergeSort(arr, mid + 1, high)
        count += self.countPairs(arr, low, mid, high)
        self.merge(arr, low, mid, high)

        return count

    def reversePairs(self, nums):
        return self.mergeSort(nums, 0, len(nums) - 1)

a = [1,3,2,3,1]

print(Solution().reversePairs(a))




'''
class Solution:
    def reversePairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] > 2*nums[j]:
                    count += 1
                    print([nums[i],nums[j]])
        return count

s = Solution()
a = s.reversePairs([1,3,2,3,1])
print(a)
'''