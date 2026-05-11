class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cons = []
        current = 1
        nums = [num for num in set(nums)]
        nums.sort()
        
        if len(nums) >= 1:
            for i in range(len(nums) - 1):
                pointer = nums[i]
                if pointer + 1 == nums[i+1] and pointer != nums[i+1]:
                    current += 1
                else:
                    max_cons.append(current)
                    current = 1
            max_cons.append(current)
            return max(max_cons)
        return 0