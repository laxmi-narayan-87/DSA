class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left = [0] * n
        right = [0] * n

        max_left = 0
        for i in range(n):
            max_left = max(max_left, height[i])
            left[i] = max_left

        max_right = 0
        for i in reversed(range(n)):
            max_right = max(max_right, height[i])
            right[i] = max_right

        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]

        return water