class Solution:
    def reverseNumber(self, n):
        rev = 0
        while n>0:
            r = n%10
            rev = rev*10 +r
            n = n//10
        print(rev)
        

s = Solution()
s.reverseNumber(52)

#TC: O(log n)
#SP: O(1)




#tried with list
"""class Solution:
    def reverseNumber(self, n):
        l = []
        while n>0:
            r = n%10
            l.append(r)
            n = n//10
        
        for i in l:
            print(i,end="")

s = Solution()
s.reverseNumber(52)
            """