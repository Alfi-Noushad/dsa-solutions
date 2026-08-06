class Solution:
    def subsequence(self,s,index,current_sum,k):
        if index == len(s):
            if current_sum == k:
                return 1
            return 0

        left = self.subsequence(s,index+1,current_sum + s[index],k)
        right = self.subsequence(s,index+1,current_sum,k)

        return left + right

s = Solution()
sa = [1,2,1]
k=2 
print(s.subsequence(sa, 0, 0, k))