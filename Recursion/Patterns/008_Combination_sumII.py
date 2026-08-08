class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        def solve(index, current_sum, current_list):
            if current_sum == target:
                ans.append(current_list[:])
                return

            if index == len(candidates):
                return

            if current_sum > target:
                return
            
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                current_list.append(candidates[i])
                solve(i+1, current_sum + candidates[i], current_list)

                # Backtrack
                current_list.pop()

        solve(0, 0, [])
        return ans
        