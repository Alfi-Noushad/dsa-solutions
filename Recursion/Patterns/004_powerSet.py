class Solution:
    def powerSet(self,s,index,current):

        if index == len(s):
            print(current)
            return
        #include current character
        self.powerSet(s,index+1,current + s[index])

        #exclude current character
        self.powerSet(s,index+1,current)

s = Solution()
s.powerSet("abc",0,"")