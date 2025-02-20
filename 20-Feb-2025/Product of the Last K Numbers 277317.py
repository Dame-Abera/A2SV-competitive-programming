# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.stream=[]
        self.prepro=[1]
           
    def add(self, num: int) -> None:
        self.stream.append(num)
        if  num==0:
            self.prepro=[1]
        else:
            self.prepro.append(self.prepro[-1]*num)     
    def getProduct(self, k: int) -> int:
        return self.prepro[-1]//self.prepro[len(self.prepro)-k-1] if  k<len(self.prepro) else  0
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)