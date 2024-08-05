class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_table = {}

        for i in range(len(nums)):

            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1

        hash_table = {key: value for key, value in sorted(hash_table.items(), key=lambda item: item[1],reverse=True)}

        result = []

        for key,value in hash_table.items():
            if k == 0:
                break
            result.append(key)
            k -= 1

        return result


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter,defaultdict

        count = Counter(count)

        hash_table = defaultdict(list)

        for key,value in count.items():
            hash_table[value].append(key)

        result = []

        for key,value in hash_table.items():
            if k == 0:
                break

            result.append(value)
            k -= 1

        return result