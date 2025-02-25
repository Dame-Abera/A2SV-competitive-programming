# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.browse=Node(homepage)
    
    def visit(self, url: str) -> None:
        self.browse.next=Node(url)
        self.browse.next.prev=self.browse
        self.browse=self.browse.next
    def back(self, steps: int) -> str:
        
        while  self.browse.prev and steps:
            self.browse=self.browse.prev
            steps-=1
            print(self.browse.val)
        return self.browse.val

                
        

    def forward(self, steps: int) -> str:
        while self.browse and self.browse.next and steps:
            self.browse=self.browse.next
            steps-=1
        return self.browse.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)