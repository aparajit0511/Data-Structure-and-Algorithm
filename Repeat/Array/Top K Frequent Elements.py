class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}

        for i in range(len(nums)):

            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1

        hash_table = {key: value for key, value in sorted(hash_table.items(), key=lambda item: item[1],reverse=True)}

        result = list(hash_table.keys())

        return result[:k]



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter, defaultdict

        count = Counter(nums) # taking count of every number

        bucket = defaultdict(list)

        for key,value in count.items():
            bucket[value].append(key)

        # creating another hash to map the count with the number in increasing order

        result = []

        # run loop in reverse to find k most frequent

        for i in range(len(nums),-1,-1):

            result.extend(bucket[i])

            if len(result) == k:
                return result

        return result

