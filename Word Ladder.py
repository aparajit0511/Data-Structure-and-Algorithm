# Time Complexity: 𝑂 ( m * n * 26)
# Space Complexity: 𝑂 ( n )

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        alphabets = []
        for i in range(ord('a'), ord('z') + 1):
            alphabets.append(chr(i))

        wordList = set(wordList)
        print(wordList)

        if endWord not in wordList:
            return 0

        from collections import deque
        queue = deque()

        count_length = 1

        queue.append((beginWord,count_length))

        # if beginWord in wordList:
        #     wordList.remove(beginWord)

        while queue:

            item,count_length = queue.popleft()

            if item == endWord:
                return count_length

            for i in range(len(item)):
                for j in alphabets:

                    new_word = item[:i] + j + item[i+1:]

                    if new_word in wordList:
                        
                        wordList.remove(new_word)
                        queue.append((new_word,count_length+1))
                        

        return 0

