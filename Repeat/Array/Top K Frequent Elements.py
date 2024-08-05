# Time Complexity: O(NLogN) and Space Complexity: O(N)
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


# Time Complexity: O(N) and Space Complexity: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter,defaultdict

        count = Counter(nums)

        hash_table = defaultdict(list)

        for key,value in count.items():
            hash_table[value].append(key)

        result = []
        print(hash_table)

        for freq in range(len(nums),-1,-1):

            if freq in hash_table:
                result.extend(hash_table[freq])
                
                if len(result) == k:
                    break


        return result

