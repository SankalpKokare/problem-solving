class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        inc = dec = True

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                dec = False
            elif nums[i - 1] > nums[i]:
                inc = False

        return inc or dec
