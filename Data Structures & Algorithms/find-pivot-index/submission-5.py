class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = nums[i] + prefix[i]

        for i in range(len(nums)):
            prefix_sum = prefix[i]
            suffix_sum = prefix[len(nums)] - prefix[i + 1]

            if prefix_sum == suffix_sum:
                return i

        return -1
