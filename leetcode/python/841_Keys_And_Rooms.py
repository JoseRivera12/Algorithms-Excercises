class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        visited = set()
        
        queue.append(rooms[0])
        visited.add(0)
        
        while queue:
            nexts = queue.popleft()
            for room in nexts:
                if room not in visited:
                    queue.append(rooms[room])
                    visited.add(room)
        
        return len(visited) == len(rooms)
