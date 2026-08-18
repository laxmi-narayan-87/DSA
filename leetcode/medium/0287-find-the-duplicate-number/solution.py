class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            # dig=nums[i]
            # for j in range(i+1,n):
            #     if nums[j]==dig:
            #         return dig
            val=abs(nums[i])
            if nums[val]<0:
                return abs(nums[i])
            else:
                nums[val]*=-1
        for i in range(n):
            if nums[i]<0:
                nums[i]*=-1
