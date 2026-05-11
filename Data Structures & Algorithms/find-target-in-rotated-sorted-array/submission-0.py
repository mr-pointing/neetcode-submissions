class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom, top = 0, len(nums) - 1

        while bottom < top:
            mid = (top + bottom) // 2
            if nums[mid] > nums[top]:
                bottom = mid + 1
            else:
                top = mid

        pivot = bottom

        def binary_search(l: int, r: int) -> int:
            while l <= r:
                middle = (l + r) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    r = middle - 1
                else:
                    l = middle + 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        return binary_search(pivot, len(nums) - 1)