class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        hash_table = defaultdict()
        result = []

        for word in words:
            item = ''.join(sorted(word))
            if item not in hash_table:
                hash_table[item] = [word]
            else:
                hash_table[item].append(word)

        for key,value in hash_table.items():
            result.append(value)

        return result

