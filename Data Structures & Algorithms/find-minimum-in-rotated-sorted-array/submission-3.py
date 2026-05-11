class Solution:
    def findMin(self, nums: List[int]) -> int:
        bottom, top = 0, len(nums) - 1
        stack = []

        while bottom <= top:
            mid = (top + bottom) // 2

            if nums[bottom] < nums[mid] > nums[top]:
                stack.append(nums[mid])
                bottom = mid + 1
            elif nums[bottom] > nums[mid]:
                top = mid - 1
            else:
                stack.append(nums[mid])
                bottom = mid + 1
        if nums.index(max(stack)) >= len(nums) - 1:
            return nums[0]
        else:
            return nums[nums.index(max(stack)) + 1]