'''
Kahn's topological sort
'''

from collections import defaultdict, deque

class Graph:
    def __init__(self,v,edges):
        self.V= v
        self.adj_list=defaultdict(list)
        self.in_dependencies=[0]* v
        for u,v in edges:
            self.adj_list[u].append(v)
            self.in_dependencies[v]+=1
    
    def kahns_topological_sort(self):
        topological_sort=[]
        q=deque([i for i in self.adj_list if self.in_dependencies[i]==0])
        while q:
            item = q.popleft()
            topological_sort.append(item)
            for neighbour in self.adj_list[item]:
                self.in_dependencies[neighbour]-=1
                if self.in_dependencies[neighbour]==0:
                    q.append(neighbour)
        if len(topological_sort)!=self.V:
            print('Cycles found. Cannot sort topologically')
        else:
            print(topological_sort)

g = Graph(6,[(5, 0), (5, 2),(4, 0), (4, 1), (2, 3), (3, 1)])
g.kahns_topological_sort()