class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        stack = []
        bottom, top = 1, max(piles)

        while bottom <= top:
            count = 0
            mid = (top + bottom) // 2
            for pile in piles:
                count += math.ceil((float(pile)/mid))
            if count > h:
                bottom = mid + 1
                continue
            elif count <= h:
                stack.append(mid)
                top = mid - 1

        return min(stack)
                
