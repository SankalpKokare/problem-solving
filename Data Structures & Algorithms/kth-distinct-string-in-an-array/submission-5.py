class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        count = Counter(arr)

        for n in arr:
            if count[n] == 1:
                k -= 1

            if k == 0:
                return n

        return ""
