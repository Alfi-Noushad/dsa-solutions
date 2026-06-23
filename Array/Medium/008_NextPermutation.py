class Solution:
    def nextPermutation(self, arr):
        for i in range(len(arr)-2,-1,-1):
            if arr[i] < arr[i+1]:
                for j in range(len(arr)-1,i,-1):
                    if arr[i] < arr[j]:
                        arr[i],arr[j] = arr[j],arr[i]
                        left = i + 1
                        right = len(arr) - 1
                        while left < right:
                            arr[left],arr[right] = arr[right],arr[left]
                            left+=1
                            right-=1
                        return arr

        left = 0
        right = len(arr)-1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1  
        return arr            
            
        
s = Solution()
a = s.nextPermutation([1, 2, 7, 4, 3, 1])
print(a)
                        
