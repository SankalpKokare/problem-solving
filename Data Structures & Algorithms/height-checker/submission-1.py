class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count_height = defaultdict(int)

        for h in heights:
            count_height[h] += 1

        expected = []

        for h in range(1, 101):
            c = count_height[h]
            for _ in range(c):
                expected.append(h)

        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1

        return res
