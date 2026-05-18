class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count_height = Counter(heights)
        res = 0
        expected = []

        for i in range(1, 101):
            for _ in range(count_height[i]):
                expected.append(i)

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1

        return res
