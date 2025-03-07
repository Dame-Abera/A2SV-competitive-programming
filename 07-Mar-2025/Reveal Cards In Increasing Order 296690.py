# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue=deque()
        for i  in deck:
            if queue:
                a=queue.pop()
                queue.appendleft(a)
            queue.appendleft(i)    
        return list(queue)    