class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        uniq = set(nums)
        res = []

        for i in range(1, len(nums) + 1):
            if i not in uniq:
                res.append(i)

        return res
