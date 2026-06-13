class Solution:
    def pattern11(self, n):
        for i in range(1,n+1):
            if i % 2 != 0: #odd->1
                num = 1
            else:          #even->0
                num = 0
                    
            for j in range(i):
                print(num,end="")
                num = 1 - num         #swaps btw 0 & 1 ...
                
            print()


c = Solution()
c.pattern11(4)



"""
1
01
101
0101

"""