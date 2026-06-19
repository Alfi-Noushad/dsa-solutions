class Solution:
    def unionArray(self, arr1, arr2):
        i = 0
        j = 0
        ans = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                if len(ans) == 0 or ans[-1] != arr1[i]:
                    ans.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if len(ans) == 0 or ans[-1] != arr2[j]:
                    ans.append(arr2[j])
                j += 1
            else:
                if len(ans) == 0 or ans[-1] != arr1[i]:
                    ans.append(arr1[i])
                j += 1
                i += 1

        while i < len(arr1):
            if len(ans) == 0 or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i += 1

        while j < len(arr2):
            if len(ans) == 0 or ans[-1] != arr2[j]:
                ans.append(arr2[j])
            j += 1

        print(ans)


s = Solution()
s.unionArray([1, 2, 3, 4, 5],[1, 2, 7])








"""
class Solution:
    def unionArray(self, arr1, arr2):
        val = set(arr1) | set(arr2)

        val = sorted(val)

        print(val)

s = Solution()
s.unionArray([1, 2, 3, 4, 5],[1, 2, 7])
"""
