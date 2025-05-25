'''
topological sort: DAGs
'''


class Graph:
    def __init__(self,V):
        self.V=V
        self.adj_list={i:[] for i in range(V)}
    
    def add_edge(self,u,v):
        self.adj_list[u].append(v)
    
    def _topological_sort_util(self,node,stack,visited):
        visited[node]=True
        for neighbour in self.adj_list[node]:
            if not visited[neighbour]:
                self._topological_sort_util(neighbour,stack,visited)
        stack.append(node)

    def topological_sort(self):
        stack=[]
        visited=[False]*self.V
        for v in range(self.V):
            if not visited[v]:
                self._topological_sort_util(v,stack,visited)
        print('...Topological sort...')
        print(stack[::-1])

# Example usage
g = Graph(6)
g.add_edge(5, 0)
g.add_edge(5, 2)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()