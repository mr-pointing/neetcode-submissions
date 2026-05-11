class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mrow, mcol = len(matrix), len(matrix[0])

        l, r  = 0, mrow - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break

        if not (l <= r):
            return False

        low, high = 0, len(matrix[m])
        while low <= high:
            mid = (low + high) // 2
            if target == matrix[m][mid]:
                return True
            elif target > matrix[m][mid]:
                low = mid + 1
            else: 
                high = mid - 1
        return False
            