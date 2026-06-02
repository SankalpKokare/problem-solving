class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indx = {}
        res = []

        for i, n in enumerate(nums):
            if target - n in num_indx:
                return [num_indx[target - n], i]
            num_indx[n] = i

        return []
