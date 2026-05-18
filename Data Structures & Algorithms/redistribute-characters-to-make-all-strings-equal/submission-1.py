class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char = defaultdict(int)

        for w in words:
            for c in w:
                char[c] += 1

        for c in char:
            if char[c] % len(words) != 0:
                return False

        return True
