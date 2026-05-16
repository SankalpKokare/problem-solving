class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_character = Counter(chars)
        res = 0

        for w in words:
            wcount = Counter(w)
            good = True

            for c in w:
                if wcount[c] > total_character[c]:
                    good = False
                    break

            res += len(w) if good else 0

        return res
