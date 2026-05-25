class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        count = defaultdict(int)

        for w in words:
            for c in w:
                count[c] += 1

        for k in count:
            if count[k] % len(words) != 0:
                return False

        return True
