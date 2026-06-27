class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m-1
        j = n-1
        k = m + n - 1

        while i >= 0 and j >=0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

            else:
                nums1[k] = nums1[i]
                k -=  1
                i -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        
        return nums1

s = Solution()
nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]
m = 4
n = len(nums2)
a = s.merge(nums1,m,nums2,n)
print(a)