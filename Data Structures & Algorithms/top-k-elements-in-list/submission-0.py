from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        # Counter O(n)
        encounters = defaultdict(int)

        for number in nums:
            encounters[number] = encounters[number] +1

        # BucketSort O(n)
        buckets = [0]*(len(nums)+1)
        for number, hits in encounters.items():
            buckets[hits] = number

        # Get top k elements which are not null O(n)
        result = []
        while len(result) < k:
            head = buckets.pop()
            if head != 0:
                result.append(head)

        return result