class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        for x in nums:
            total_xor ^= x

        if total_xor != 0:
            return len(nums)

        for x in nums:
            if x != 0:
                return len(nums) - 1

        return 0