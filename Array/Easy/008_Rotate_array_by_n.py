class Solution:
    def rotateArrayByn(self, arr,n):
        n = n % len(arr)
        temp = []
        for i in range(n):
            temp.append(arr[i])
        
        for i in range(0,len(arr)-n):
            arr[i] = arr[n+i]
        for i in range(len(temp)):
            arr[len(arr)-n + i] = temp[i]
    
        print(arr)


s = Solution()
s.rotateArrayByn([1, 2, 3, 4, 5,6],2)











"""
class Solution:
    def rotateArrayByn(self, arr,n):
        for i in range(n):
            temp = arr[0]
            for i in range(len(arr)-1):
                arr[i] = arr[i+1]
            arr[len(arr)-1] = temp
    
        print(arr)


s = Solution()
s.rotateArrayByn([1, 2, 3, 4, 5,6],2)

"""
