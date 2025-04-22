# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q=deque()
        q.append(0)
        visited=set()
        visited.add(0)
        while q:
            for i  in range(len(q)):
                a=q.popleft()
                for i  in rooms[a]:
                    if i not in visited:
                        visited.add(i)
                        q.append(i)
        print(visited)                
        return len(visited)==len(rooms)   

                         



                       