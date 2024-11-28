class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        hash_table = {}

        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1

        hash_table = {key:value for key,value in sorted(hash_table.items(), key=lambda item:item[1],reverse=True)}

        for key,value in hash_table.items():

            if len(result) == k:
                break

            result.append(key)

        return result



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter,defaultdict

        count = Counter(nums)

        hash_table = defaultdict(list)
        result = []

        for key,value in count.items():
            hash_table[value].append(key)

        for freq in range(len(nums),-1,-1):
            if freq in hash_table:
                result.extend(hash_table[freq])

                if len(result) == k:
                    break

        return result





class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort(reverse=True)

        return nums[k-1]

