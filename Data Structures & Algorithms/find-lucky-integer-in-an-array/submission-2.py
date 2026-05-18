class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = -1

        for i in range(len(arr)):
            if arr[i] == count[arr[i]]:
                res = max(arr[i], res)

        return res
