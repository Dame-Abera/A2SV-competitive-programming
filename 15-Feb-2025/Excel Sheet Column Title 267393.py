# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        while(columnNumber>0):
            offset=(columnNumber-1)%26
            res+=chr(ord('A')+offset)
            columnNumber=(columnNumber-1)//26
        return res[::-1]