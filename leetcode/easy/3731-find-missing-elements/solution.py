class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num=sorted(nums)
        mis=[]
        for i in range(num[0],num[len(nums)-1]):
            if i not in nums:
                mis.append(i)
        return mis