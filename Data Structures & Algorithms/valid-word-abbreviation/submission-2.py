class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            # invalid
            if abbr[j] == "0":
                return False
            # parse number
            if abbr[j].isdigit():
                sublen = 0
                while j < len(abbr) and abbr[j].isdigit():
                    sublen = sublen * 10 + int(abbr[j])
                    j += 1
                i += sublen  # skip character

            # if letter
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)
