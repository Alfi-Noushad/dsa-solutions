class Solution:
    def moveZeroes(self, arr):
        j = -1
        for i in range(len(arr)):
            if arr[i] == 0:
                j = i
                break

        i = j+1
        for i in range(j + 1,len(arr)):
            if arr[i] != 0 and arr[j] == 0:
                arr[j],arr[i] = arr[i],arr[j]
                j += 1

        print(arr)

s = Solution()
s.moveZeroes([1 ,0 ,2 ,3 ,0 ,4 ,0 ,1])









""" brute force
class Solution:
    def moveZeroes(self, arr):
        temp = []
        for i in range(len(arr)):
            if arr[i] != 0:
                temp.append(arr[i])
        
        for i in range(len(temp)):
                arr[i] = temp[i]

        for i in range(len(temp),len(arr)):
                arr[i] = 0

        print(arr)

s = Solution()
s.moveZeroes([1 ,0 ,2 ,3 ,0 ,4 ,0 ,1])

"""
