class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for i, n in enumerate(nums):
            if target - n in num_index:
                return [num_index[target - n], i]

            num_index[n] = i

        return []
