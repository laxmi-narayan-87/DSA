class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        hq = []
        for wt in workerTimes:
            heapq.heappush(hq, (wt, wt, 2))
        t = 0
        while mountainHeight>0:
            curr_t = hq[0][0]
            while hq and hq[0][0]==curr_t:
                _, wt, mul = heapq.heappop(hq)
                nxt_t = curr_t+(mul*wt)
                nxt_mul = mul+1
                heapq.heappush(hq, (nxt_t, wt, nxt_mul))
                mountainHeight-=1
        return curr_t