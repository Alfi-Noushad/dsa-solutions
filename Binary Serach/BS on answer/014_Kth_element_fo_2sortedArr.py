class Solution:
    def kthElement(self, a, b, k):
        l = 0
        r = 0
        count = 0
        current = 0

        while l < len(a) and r < len(b):
            if a[l] < b[r]:
                current = a[l]
                l+=1
            else:
                current = a[r]
                r+= 1
            count += 1
        
            if count == k:
                return current
        while count <= k and l < len(a):
            current = a[l]
            l+=1
            count += 1
        while count <= k and r < len(b):
            current = b[r]
            r+=1
            count += 1
        
        return current

s =Solution()
a = s.kthElement([2, 3, 6, 7, 9],[1, 4, 8, 10],5)
print(a)
        