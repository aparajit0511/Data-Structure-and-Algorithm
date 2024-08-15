class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        from collections import deque
        queue = deque()

        queue.append((beginWord,1))
        wordList = set(wordList)

        while queue:

            word,length = queue.popleft()

            if word == endWord:
                return length

            for w in range(len(word)):
                for alphabet in "abcdefghijklmnopqrstuvwxyz":

                    new_word = word[:w] + alphabet + word[w+1:]
                    # print(new_word)
                    if new_word in wordList:
                        queue.append((new_word,length+1))
                        wordList.remove(new_word)

        return 0