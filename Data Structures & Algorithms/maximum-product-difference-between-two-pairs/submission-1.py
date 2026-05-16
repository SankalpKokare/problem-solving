class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        highestmax, highmax = 0, 0
        lowestmin, lowmin = float("inf"), float("inf")
        res = 0

        for n in nums:
            if n > highestmax:
                highestmax, highmax = n, highestmax
            elif n > highmax:
                highmax = n

            if n < lowestmin:
                lowestmin, lowmin = n, lowestmin
            elif n < lowmin:
                lowmin = n

        return (highestmax * highmax) - (lowestmin * lowmin)
