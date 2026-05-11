class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        l, r = 0, k - 1

        while r < len(nums):
            stack.append(max(nums[l:r + 1]))
            l += 1
            r += 1

        return stack
