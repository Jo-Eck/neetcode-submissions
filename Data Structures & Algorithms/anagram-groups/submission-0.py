from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def normalizeWord(word: str) -> list[int]:
            letterCounter = [0]*26
            for letter in word:
                index = ord(letter)-97
                letterCounter[index] = letterCounter[index]+1
            return ''.join(map(str,letterCounter))
        

        anagramGroups = defaultdict(list)

        for word in strs:
            anagramGroups[normalizeWord(word)].append(word)            

        return list(anagramGroups.values())