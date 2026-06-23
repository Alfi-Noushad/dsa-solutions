class Solution:
    def rearrangeArray(self, arr):
        n = len(arr)
        pos = 0
        neg = 1
        ans = [0]*n

        for i in arr:
            if i > 0:
                ans[pos] = i
                pos += 2
            else:
                ans[neg] = i
                neg += 2
        return ans
    
s =  Solution()
a = s.rearrangeArray([1, 2, -3, -1, -2, 3])
print(a)


'''
class Solution:
    def rearrangeArray(self, arr):
        pos = []
        neg = []
        ans = []
        for i in range(len(arr)):
            if arr[i] > 0:
                pos.append(arr[i])
            else: 
                neg.append(arr[i])
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])

        return ans
    
s =  Solution()
a = s.rearrangeArray([1, 2, -3, -1, -2, 3])
print(a)

'''
