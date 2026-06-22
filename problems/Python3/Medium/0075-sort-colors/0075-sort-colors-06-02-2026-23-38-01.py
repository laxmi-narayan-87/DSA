class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        cat0,cat1,cat2 =0,0,0
        for i in range(n):
            if nums[i]==0:
                cat0+=1
            elif nums[i]==1:
                cat1+=1
            else:
                cat2+=1
        for i in range(cat0):
            nums[i]=0
        for i in range(cat0,cat0+cat1):
            nums[i]=1
        for i in range(cat0+cat1,n):
            nums[i]=2
        return