class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1  # cannot be 0
        r = max(piles)
        
        while l <= r:
            mid = (l + r) // 2
            if self.check(piles, mid, h):
                r = mid - 1
            else:
                l = mid + 1

        return l

    def check(self, piles, rate, h):
        # calculate total hours needed without modifying original piles
        hours_needed = 0
        for pile in piles:
            # ceil division: how many hours to eat this pile at rate `rate`
            hours_needed += (pile + rate - 1) // rate
        return hours_needed <= h
