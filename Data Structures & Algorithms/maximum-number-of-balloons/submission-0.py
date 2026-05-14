class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countext = Counter(text)
        balloon = Counter("balloon")

        res = len(text)

        for c in balloon:
            res = min(res, countext[c] // balloon[c])

        return res
