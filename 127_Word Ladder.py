# Name: 127. Word Ladder
# Link: https://leetcode.com/problems/word-ladder/
# Time: 11/24/2020
import collections
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        q = collections.deque()
        q.append((beginWord, 1))
        while q:
            curWord, l = q.popleft()
            if curWord == endWord:
                return l
            for i in range(len(curWord)):
                for c in 'abcdefghijkmlnopqrstuvwxyz':
                    newWord = curWord[:i] + c + curWord[i+1:]
                    if newWord in wordList and newWord != curWord:
                        wordList.remove(newWord)
                        q.append((newWord, l+1))
        return 0

if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

