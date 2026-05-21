class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_chars = Counter(chars)
        res = 0
        for w in words:
            c_chars = Counter(w)
            good = True
            for c in w:
                if c_chars[c] > count_chars[c]:
                    good = False
                    break
            if good:
                res += len(w)

        return res
