from collections import deque

class Graph:
    def __init__(self):
        self.adj_list={}
    
    def add_edge(self,u,v):
        self.adj_list.setdefault(u,[]).append(v)
        self.adj_list.setdefault(v,[]).append(u)
    
    def bfs(self,start_node):
        if start_node not in self.adj_list.keys():
            return None
        visited = set()
        q=deque([start_node])
        visited.add(start_node)
        while q:
            item = q.popleft()
            print(item, end=" ")
            for k in self.adj_list[item]:
                if k not in visited:
                    q.append(k)
                    visited.add(k)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

print("BFS traversal starting from node 0:")
g.bfs(0)