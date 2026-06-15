class Solution:    
    def fib(self, n):
        a=0
        b=1
        for i in range(n):
            print(a,end="")
            a,b = b, a+b

s = Solution()
s.fib(5)
        
#TC: O(n)
#SC: O(1)
