class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        highest = high = float("-inf")
        smallest = small = float("inf")

        for n in nums:
            if n > highest:
                highest, high = n, highest
            elif n > high:
                high = n

            if n < smallest:
                smallest, small = n, smallest
            elif n < small:
                small = n

        return (highest * high) - (smallest * small)
