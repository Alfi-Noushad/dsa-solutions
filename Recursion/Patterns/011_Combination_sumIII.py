class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        def solve(index,current_sum,current_list):
            if current_sum == n and len(current_list) == k:
                ans.append(current_list[:])
                return
            if current_sum > n:
                return
            if len(current_list) == k:
                return
            for i in range(index,10):
                current_list.append(i)
                solve(i+1,current_sum + i ,current_list)
                current_list.pop()
        solve(1,0,[])
        return ans

        