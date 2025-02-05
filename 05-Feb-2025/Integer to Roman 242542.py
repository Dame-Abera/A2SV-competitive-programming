# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        string=""
        while num>0:
            print(num)
            count=3
            while num>=1000:
                string+="M"
                num-=1000
            while num>=500:
                if num>=900:
                    string+="CM"
                    num-=900
                else:    
                 string+="D"    
                 num-=500
                break

            while num>=100:
                if num>=400:
                    string+="CD"
                    num-=400
                else:    
                    string+="C"  
                    num-=100
            while num>=50:
                if num>=90:
                    string+="XC"
                    num-=90
                else:
                    string+="L"  
                    num-=50
                break
            while num>=10:
                if num>=40:
                    string+="XL"
                    num-=40
                else:
                    string+="X" 
                    num-=10
                print(num)
            while num>=5:
                if num>=9:
                    string+="IX"
                    num-=9
                else:    
                    string+="V"    
                    num-=5
                break
            while num>=1:
                if num>=4:
                    string+="IV"
                    num-=4
                else:
                    string+="I"   
                    num-=1
            print(num)    
        return string                
