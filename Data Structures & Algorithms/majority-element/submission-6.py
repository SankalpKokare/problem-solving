class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        cur_no = 0

        for i in range(len(nums)):
            if cur_no == 0:
                res = nums[i]
            cur_no += 1 if nums[i] == res else -1

        return res
