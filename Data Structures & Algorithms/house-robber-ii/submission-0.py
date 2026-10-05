class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev1 = 0
            prev2 = 0

            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current

            return prev1

        # Case 1: Don't rob the first house
        case1 = rob_linear(nums[1:])

        # Case 2: Don't rob the last house
        case2 = rob_linear(nums[:-1])

        return max(case1, case2)