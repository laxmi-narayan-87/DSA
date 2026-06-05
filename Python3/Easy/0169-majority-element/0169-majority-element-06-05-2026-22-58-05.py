class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate =None
        count=0
        n=len(nums)
        threshold=n//2
        for num in nums:
            if count == 0:
                candidate=num
            count += 1 if num == candidate else -1
            if count>threshold:
                break
        if nums.count(candidate)>n//2:
            return candidate
        return -1