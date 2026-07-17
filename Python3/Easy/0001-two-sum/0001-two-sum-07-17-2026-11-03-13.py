class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]+nums[j])== target:
                    return [i,j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            complement =target-nums[i]
            for j in range(n):
                if complement == nums[j] and i!=j:
                    return [i,j]