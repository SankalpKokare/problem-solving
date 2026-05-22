class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        highest = high = float("-inf")
        lowest = low = float("inf")

        for i in range(len(nums)):
            if nums[i] > highest:
                highest, high = nums[i], highest
            elif nums[i] > high:
                high = nums[i]

            if nums[i] < lowest:
                lowest, low = nums[i], lowest
            elif nums[i] < low:
                low = nums[i]

        return (highest * high) - (lowest * low)
