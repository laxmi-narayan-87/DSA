class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]+nums[j])== target:
                    return [i,j]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            complement =target-nums[i]
            for j in range(n):
                if complement == nums[j] and i!=j:
                    return [i,j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,val in enumerate(nums):
            hashmap[val] =i
        
        for i,val in enumerate(nums):
            complement= target-nums[i]
            if complement in hashmap and hashmap[complement] !=i:
                return [i,hashmap[complement]]