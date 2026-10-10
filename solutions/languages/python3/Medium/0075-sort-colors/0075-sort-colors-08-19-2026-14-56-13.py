class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cat0=nums.count(0)
        cat1=nums.count(1)
        cat2=nums.count(2)
        for i in range(len(nums)):
            if i<cat0:
                nums[i]=0
            elif cat0<=i<cat0+cat1:
                nums[i]=1
            elif i>=(cat0+cat1):
                nums[i]=2
        return nums