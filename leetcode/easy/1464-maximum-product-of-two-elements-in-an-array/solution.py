class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        max1=max2=1
        for i in range(n):
            if nums[i]>max1:
                max2=max1
                max1=nums[i]
            elif max2<nums[i]:
                max2=nums[i]
        return (max1-1)*(max2-1)