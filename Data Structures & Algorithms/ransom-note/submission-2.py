class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ran = Counter(ransomNote)
        count_mag = Counter(magazine)

        for c in count_ran:
            if count_ran[c] > count_mag[c]:
                return False

        return True
