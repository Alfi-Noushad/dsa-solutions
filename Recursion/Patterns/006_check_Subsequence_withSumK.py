class Solution:
    def countSub(self,s,index,current_sum,k):

        if index == len(s):
            return current_sum == k

        take = self.countSub(s,index+1,current_sum + s[index],k)

        skip = self.countSub(s,index+1,current_sum,k)

        return take or skip

s = Solution()
print(s.countSub([1,2,3,4,5],0,0,8))