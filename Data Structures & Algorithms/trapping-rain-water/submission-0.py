class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = {}
        right = {}
        i = 1
        while i < len(height):
            left[i] = max(height[:i])
            right[i] = max(height[i:])
            if height[i] <= min(left[i], right[i]):
                res += min(left[i], right[i]) - height[i]
            i += 1
        return res