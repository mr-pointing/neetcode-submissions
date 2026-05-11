class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        while i < len(nums):
            product = 1
            new = nums.copy()
            new.pop(i)
            for new_num in new:
                product *= new_num
            output.append(product)
            i += 1
        return output