class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        for i in range(len(nums)):
            prefix = prefix_sum[i]
            suffix = prefix_sum[len(nums)] - prefix_sum[i + 1]
            if prefix == suffix:
                return i

        return -1
