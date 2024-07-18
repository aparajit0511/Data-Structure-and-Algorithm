# Time Complexity: 𝑂 ( 𝑛 ⋅ 4 ^ 𝑛 )
# Space Complexity: 𝑂 ( 4 ^ 𝑛 )

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        directory = {
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"],
        }

        result = []

        result.extend(directory[digits[0]])

        print(result)

        for digit in digits[1:]:
            combination = []

            for item in directory[digit]:
                for res in result:
                    new_item = res + item
                    combination.append(new_item)

            result = combination

        return result
