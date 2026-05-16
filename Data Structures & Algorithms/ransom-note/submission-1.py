class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countRwords = Counter(ransomNote)
        countMwords = Counter(magazine)

        for r in countRwords.keys():
            if countMwords[r] < countRwords[r]:
                return False

        return True
