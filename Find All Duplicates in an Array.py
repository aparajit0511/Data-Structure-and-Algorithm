# Time Complexity: O(n * 2) and Space Complexity: O(k)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        result = set()

        for i in range(len(nums)):
            count = 1
            for j in range(i+1,len(nums)):
                if nums[j] == nums[i]:
                    count += 1

            if count == 2 and nums[i] not in result:
                result.add(nums[i])

        return list(result)

# Time Complexity: O(N) and Space Complexity: O(N)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()

        hash_table = {}

        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1
                
        print(hash_table)

        for keys,value in hash_table.items():
            if hash_table[keys] == 2 and keys not in result:
                result.add(keys)

        return list(result)


# Time Complexity: O(N) and Space Complexity: O(1)
# chatgpt solution
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()

        for num in nums:
            index = abs(num) - 1  # Convert to 0-based index
            if nums[index] < 0:
                result.add(abs(num))
            else:
                nums[index] = -nums[index]

        return list(result)
