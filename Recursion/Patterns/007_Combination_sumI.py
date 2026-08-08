class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def solve(index, current_sum, current_list):
            if current_sum == target:
                ans.append(current_list[:])
                return

            if index == len(candidates):
                return

            if current_sum > target:
                return

            # Take the current candidate
            current_list.append(candidates[index])
            solve(index, current_sum + candidates[index], current_list)

            # Backtrack
            current_list.pop()

            # Skip the current candidate
            solve(index + 1, current_sum, current_list)

        solve(0, 0, [])
        return ans