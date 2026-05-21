class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        res = []
        data = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in data:
                res.append(i)

        return res
