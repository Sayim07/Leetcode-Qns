class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        low = 0
        high = 0
        r = float('inf')
        sum = 0

        while high < n:
            sum = sum + nums[high]

            while sum >= target:
                l = high - low + 1
                r = min(r, l)

                sum = sum - nums[low]
                low += 1

            high += 1

        if r == float('inf'):
            return 0

        return r