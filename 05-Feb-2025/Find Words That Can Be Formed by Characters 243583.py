# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charcount=Counter(chars)
        count=0
        for word in words:
            wordcount=Counter(word)
            for i in wordcount:
                if wordcount[i]>charcount[i]:
                    break
            else:
                count+=len(word)
        return count        