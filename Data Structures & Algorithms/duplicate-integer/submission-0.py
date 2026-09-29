class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encounteredValues = set()

        for value in nums: 
            if value in encounteredValues:
                return True
            else:
                encounteredValues.add(value)

        return False