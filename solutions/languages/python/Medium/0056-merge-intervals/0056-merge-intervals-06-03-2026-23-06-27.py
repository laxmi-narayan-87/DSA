class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        for s,e in intervals[1:]:
            if intervals[i][1]>=s:
                intervals[i][1]=max(intervals[i][1],e)
            else:
                i+=1
                intervals[i]=[s,e]
        return intervals[:i+1]