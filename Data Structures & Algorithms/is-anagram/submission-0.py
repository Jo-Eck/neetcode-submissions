class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def normalizeWord(word: str) -> list[int]:
            letterCounter = [0]*26
            for letter in word:
                index = ord(letter)-91
                letterCounter[index] = letterCounter[index]+1
            return letterCounter

        return normalizeWord(s) == normalizeWord(t)