'''
Given a directed graph and two nodes (S and E), design an algorithm to find out whether
there is a route from S to E.

BFS
'''
from collections import defaultdict, deque

class Graph:
    def __init__(self,dict):
        self.vertices=set()
        self.edges=defaultdict(list)

        for k,v in dict.items():
            self.vertices.add(k)
            self.edges[k].extend(v)
    
    def check_route_bfs(self,start,end):
        '''
        Time: O(V+E) each node and edge are visited atmost once in worst case
        Space: O(V) worst case queue size
        '''
        # generally preferred as it traverses level by level
        if start not in self.vertices or end not in self.vertices:
            return False
        visited = set()
        q = deque([start])
        while q:
            item = q.popleft()
            if item == end:
                return True
            visited.add(item)
            for neighbour in self.edges[item]:
                if not neighbour in visited:
                    q.append(neighbour)
        return False

    def check_route_dfs(self,node,end,visited=None):
        '''
        Time: O(V+E) each node and edge are visited atmost once in worst case
        Space: O(V) worst case recursion depth
        '''
        found=False
        if node not in self.vertices or end not in self.vertices:
            return found
        if not visited:
            visited=set()
        for neighbour in self.edges[node]:
            if not neighbour in visited:
                if neighbour==end:
                    return True
                else:
                    visited.add(neighbour)
                    found=self.check_route_dfs(neighbour,end,visited)
                    if found:
                        return found
        return found
    
customDict = {
    "a" : ["c","d", "b"],
    "b" : ["j"],
    "c" : ["g"],
    "d" : [],
    "e" : ["f", "a"],
    "f" : ["i"],
    "g" : ["d", "h"],
    "h" : [],
    "i" : [],
    "j" : []
}
 
g = Graph(customDict)
print(g.check_route_bfs("a", "j"))  # True
print(g.check_route_bfs("e", "j"))  # True (e -> a -> b -> j)
print(g.check_route_bfs("a", "e"))  # False (no path from a to e)

print(g.check_route_dfs("a", "j"))  # True
print(g.check_route_dfs("e", "j"))  # True (e -> a -> b -> j)
print(g.check_route_dfs("a", "e"))  # False (no path from a to e)