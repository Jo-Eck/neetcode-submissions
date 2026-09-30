from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        # Counter O(n)
        encounters = defaultdict(int)

        for number in nums:
            encounters[number] = encounters[number] +1
        # print(f"encounter: {encounters}")

        # BucketSort O(n)
        buckets = [None]*(len(nums)+1)

        for number, hits in encounters.items():
            if buckets[hits] is None:
                buckets[hits] = [number]
            else:
                buckets[hits].append(number)

        # Get top k elements which are not null O(n)
        result = []
        while len(result) < k:
            # print(f"result: {result} - buckets: {buckets}")
            head = buckets.pop()
            if head is not None:
                result.extend(head)

        return result