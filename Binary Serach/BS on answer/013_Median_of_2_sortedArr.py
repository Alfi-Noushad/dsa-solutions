class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = 0
        r = 0
        prev = 0
        current = 0
        count = 0
        total = len(nums1) + len(nums2)
        mid = total // 2
        while  l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                prev = current
                current = nums1[l]
                
                l += 1
            else:
                prev = current
                current = nums2[r]
                
                r += 1
            count += 1
            if count > mid:
                break

        while count <= mid and l < len(nums1):
            prev = current
            current = nums1[l]
            l += 1
            count += 1

        while count <= mid and r < len(nums2):
            prev = current
            current = nums2[r]
            r += 1
            count += 1

        if total % 2 == 0:
            return (current+prev)/2.0
        else:
            return current

         
        
s = Solution()
a = s.findMedianSortedArrays([2, 4, 6],[1,3,5])
print(a)








'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = 0
        r = 0
        ans = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                ans.append(nums1[l])
                l += 1
            else:
                ans.append(nums2[r])
                r += 1
        while l < len(nums1):
            ans.append(nums1[l])
            l += 1
        
        while r < len(nums2):
            ans.append(nums2[r])
            r += 1

        print(ans)
        n = len(ans)
        if n%2 == 0:
            return (ans[n//2-1]+ans[n//2])/2
        else:
            return ans[n//2]
        
s = Solution()
a = s.findMedianSortedArrays( [2, 4, 6],[1,3,5])
print(a)

'''
        