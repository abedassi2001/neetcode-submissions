class Solution:
    def rob(self, nums: list[int]) -> int:
        # Edge cases: 1 or 2 houses
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        # Helper function for a linear row of houses
        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for money in houses:
                # Max of (current + 2 houses ago) vs (1 house ago)
                current_max = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current_max
            return prev1

        # The result is the better of excluding the last house OR excluding the first
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))