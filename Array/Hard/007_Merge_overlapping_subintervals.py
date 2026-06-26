class Solution:
    def mergeOverlap(self, intervals):
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])
            
        return ans
s =Solution()
a = s.mergeOverlap([[1,3],[2,6],[8,10],[15,18]])
print(a)

