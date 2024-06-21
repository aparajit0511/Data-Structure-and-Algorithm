# Time Complexity: 𝑂 ( 𝑛 ⋅ 4 𝑛 )
# Space Complexity: 𝑂 ( 4 𝑛 )

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        hash_table = {
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]
        }

        return self.findCombinations(digits,hash_table)

    def findCombinations(self,digits,hash_table):
        if not digits:
            return []

        result = hash_table[digits[0]]

        for digit in digits[1:]:

            new_item = []
            for combination in result:
                for letter in hash_table[digit]:
                    new_item.append(combination+letter)
            result = new_item



        return result


# Time Complexity: 𝑂 ( 𝑛 ⋅ 4 𝑛 )
# Space Complexity: 𝑂 ( 4 𝑛 )

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        hash_table = {
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]
        }

        result = hash_table[digits[0]]

        return self.findCombinations(digits[1:],hash_table,result)


    def findCombinations(self,digits,hash_table,result):

        if not digits:
            return result


        new_item = []
        for letter in hash_table[digits[0]]:
            for combination in result:
                new_item.append(combination+letter)

        result = new_item[:]

        return self.findCombinations(digits[1:],hash_table,result)
        