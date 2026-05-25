class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        highest = high = float("-inf")
        lowest = low = float("inf")

        for n in nums:
            if n > highest:
                highest, high = n, highest
            elif n > high:
                high = n

            if n < lowest:
                lowest, low = n, lowest
            elif n < low:
                low = n

        return (highest * high) - (lowest * low)
