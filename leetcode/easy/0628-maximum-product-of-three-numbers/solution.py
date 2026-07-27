class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        p1=nums[0]*nums[1]*nums[n-1]
        p2=nums[n-1]*nums[n-2]*nums[n-3]
        return max(p1,p2)