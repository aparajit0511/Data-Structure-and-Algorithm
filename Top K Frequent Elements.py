## Time complexity - O(NlogN) Space Complexity - O(N)

from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        count = Counter(nums)

        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

        for key,value in count.items():
            if len(result) >= k:
                break

            result.append(key)

        return result


## ChatGPT solution
## Time complexity - O(N) Space Complexity - O(N)

from collections import Counter, defaultdict       

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        count = Counter(nums)

        bucket = defaultdict(list)

        for key,value in count.items():
            bucket[value].append(key)


        for i in range(len(nums),0,-1):
            if i in bucket:
                result.extend(bucket[i])

                if len(result) >= k:
                    break

        return result[:k]

