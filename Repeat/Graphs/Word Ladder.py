# Time Complexity: 𝑂 ( m * n * 26)
# Space Complexity: 𝑂 ( n )

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        tranform = 0

        from collections import deque
        queue = deque()
        queue.append((beginWord,0))

        while queue:
            item, count = queue.popleft()
            if item == endWord:
                return count+1
            for word in range(len(item)):
                for char in "abcdefghijklmnopqrstuvwxyz":

                    new_word = item[:word] + char + item[word+1:]

                    if new_word in wordList:
                        wordList.remove(new_word)
                        queue.append((new_word,count+1))

        return 0

