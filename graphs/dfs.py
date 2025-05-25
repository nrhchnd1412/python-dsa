
class Graph:
    def __init__(self):
        self.adj_list={}
    
    def add_edge(self,u,v):
        self.adj_list.setdefault(u,[]).append(v)
        self.adj_list.setdefault(v,[]).append(u)
    
    def dfs(self,start_node,visited=None):
        if not visited:
            visited=set()
        print(start_node,end=" ")
        visited.add(start_node)
        for k in self.adj_list[start_node]:
            if k not in visited:
                self.dfs(k,visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

print("BFS traversal starting from node 0:")
g.dfs(0)