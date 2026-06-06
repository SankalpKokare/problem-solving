class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        count = Counter(nums)

        i = 0

        for n in count:
            nums[i] = n
            count[n] -= 1
            i += 1

            if count[n] >= 1:
                nums[i] = n
                count[n] -= 1
                i += 1
        return i
