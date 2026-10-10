class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        mx=pre=cur=0
        n=len(nums)
        for i in range(n):
            cur+=1
            if i==n-1 or nums[i]>=nums[i+1]:
                if cur//2>=k or min(pre,cur) >=k:
                    return True
                pre=cur
                cur=0
        return False