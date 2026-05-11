class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for j in range(len(nums) - 1, 0, -1):
            i = 0
            while i < len(nums):
                if nums[i] + nums[j] == target:
                    sum_nums = [i, j]
                    return sum_nums
                i += 1
            
            
                