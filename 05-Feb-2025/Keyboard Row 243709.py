# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        res=[]
        for word in words:
            lword=word.lower()
            print(lword,word)
            if lword[0] in row1:
                for i in lword:
                    if i not in row1:
                        break
                else:
                      res.append(word)
            elif lword[0]  in row2:
                for i in lword:
                    if i not in row2:
                        break
                else:
                      res.append(word)
            elif lword[0]   in row3: 
                for i in lword:
                    if i not in row3:
                        break
                else:
                      res.append(word)
        return res        
