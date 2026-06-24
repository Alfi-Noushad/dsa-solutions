class Solution:
    def longestConsecutive(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        max_count = 1
        st = set()

        for i in range(n):
            st.add(arr[i])
        
        for val in st:
            if val-1 not in st:
                count = 1
                x = val

                while x+1 in st:
                    x = x+1
                    count+=1
                max_count = max(count,max_count)
        return max_count

s= Solution()
a = s.longestConsecutive([100, 4, 200, 1, 3, 2])
print(a)



'''
class Solution:
    def longestConsecutive(self, arr):
        arr.sort()
        diff = 0
        count = 1
        max_count = 1
        for i in range(1, len(arr)):
            diff = arr[i]-arr[i-1]
            if diff == 1:
                count += 1
            elif diff == 0:
                continue
            else:
                count = 1
            max_count = max(count,max_count)
        return max_count
s= Solution()
a = s.longestConsecutive([100, 4, 200, 1, 3, 2])
print(a)

'''