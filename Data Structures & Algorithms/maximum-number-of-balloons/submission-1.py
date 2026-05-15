class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        countBalloon = Counter("balloon")

        res = len(text)

        for c in countBalloon:
            cur_count = countText[c] // countBalloon[c]
            res = min(res, cur_count)

        return res
