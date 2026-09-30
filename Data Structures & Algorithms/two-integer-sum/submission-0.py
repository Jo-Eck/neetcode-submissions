class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summands = {}

        for index, value in enumerate(nums):
            if target-value in summands:
                return [summands[target-value], index]
            else:
                summands[value] = index
                
        