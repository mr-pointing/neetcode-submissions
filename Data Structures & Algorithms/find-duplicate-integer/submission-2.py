class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            id_neg = abs(num) - 1
            if nums[id_neg] < 0:
                return abs(num)
            nums[id_neg] *= -1
        return -1
        