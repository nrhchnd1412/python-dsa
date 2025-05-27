from collections import deque,defaultdict
import heapq
from typing import Dict, List, Tuple, Optional, Set

class Graph:
    '''
    Graph class which supports both directed and undirected graphs
    '''

    def __init__(self,directed=True):
        self.vertices=set()
        self.directed=directed
        self.edges=defaultdict(list)
    
    def add_vertex(self,vertex):
        self.vertices.add(vertex)
    
    def add_edge(self,u,v,weight=1):
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges[u].append((v,weight))
        if not self.directed:
            self.edges[v].append((u,weight))
    
    def get_neighbours(self,vertex):
        return self.edges[vertex]
    
def bfs_shortest_path(graph:Graph, start,end)-> Tuple[Optional[int], Optional[List]]:
    if start not in graph.vertices or end not in graph.vertices:
        return None,None
    if start==end:
        return 0,[start]
    q=deque([(start,0,[start])])
    visited={start}
    while q:
        current,distance,path=q.popleft()
        for neighbour,_ in graph.get_neighbours(current):
            if neighbour==end:
                return distance+1,path+[neighbour]
            if neighbour not in visited:
                visited.add(neighbour)
                q.append((neighbour,distance+1,path+[neighbour]))

def dijkstra_shortest_path(graph:Graph,start,end)->Tuple[Optional[int], Optional[List]]:
    if start not in graph.vertices or  end not in graph.vertices:
        return None,None
    if start == end:
        return 0, [start]
    distances={vertex:float('inf') for vertex in graph.vertices}
    distances[start]=0

    pq=[(0,start,[start])]
    visited=set()
    while pq:
        distance,current,path = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        if current==end:
            return distance,path
        for neighbour,weight in graph.get_neighbours(current):
            if neighbour not in visited:
                new_distance = distance+weight
                if new_distance<distances[neighbour]:
                    distances[neighbour]=new_distance
                    heapq.heappush(pq,(new_distance,neighbour,path+[neighbour]))
    return None, None

def bellman_ford_shortest_path(graph:Graph,start)->Tuple[Dict, Dict, bool]:
    if start not in graph.vertices:
        return {},{}, False
    
    distances = {vertex: float('inf') for vertex in graph.vertices}
    predecessors={vertex:None for vertex in graph.vertices}

    distances[start]=0

    # relax edges V-1 times
    for _ in range(len(graph.vertices)-1):
        for vertex in graph.vertices:
            if distances[vertex]!= float('inf'):
                for neighbour,weight in graph.get_neighbours(vertex):
                    if distances[vertex]+ weight < distances[neighbour]:
                        distances[neighbour]=distances[vertex]+ weight
                        predecessors[neighbour]=vertex

    #check for negative cycle
    has_negative_cycle = False
    for vertex in graph.vertices:
        if distances[vertex]!= float('inf'):
            for neighbour,weight in graph.get_neighbours(vertex):
                if distances[vertex]+ weight < distances[neighbour]:
                    has_negative_cycle=True
                    break
        if has_negative_cycle:
            break
    return distances,predecessors,has_negative_cycle

def reconstruct_path(predecessor,start,end):
    if end not in predecessor or (predecessor[end] is None and start!=end):
        return None
    '''
    predecessor looks like - {A:None,B:A,C:B,D:F...}
    '''
    current = end
    paths= []
    while current:
        paths.append(current)
        current = predecessor[current]
    paths.reverse()
    return paths if (paths and paths[0]==start) else None

print("\n=== UNWEIGHTED GRAPH - BFS vs Dijkstra ===")
g1 = Graph(directed=True)
g1.add_edge('A', 'B')
g1.add_edge('A', 'C')
g1.add_edge('B', 'D')
g1.add_edge('C', 'D')
g1.add_edge('B', 'E')
g1.add_edge('D', 'E')

bfs_dist, bfs_path = bfs_shortest_path(g1, 'A', 'E')
dijkstra_dist, dijkstra_path = dijkstra_shortest_path(g1, 'A', 'E')

print(f"BFS: Distance = {bfs_dist}, Path = {bfs_path}")
print(f"Dijkstra: Distance = {dijkstra_dist}, Path = {dijkstra_path}")

print("\n=== WEIGHTED GRAPH - Why we need Dijkstra ===")
g2 = Graph(directed=True)
g2.add_edge('A', 'B', 1)
g2.add_edge('A', 'C', 10)
g2.add_edge('B', 'C', 1)

bfs_dist, bfs_path = bfs_shortest_path(g2, 'A', 'C')
dijkstra_dist, dijkstra_path = dijkstra_shortest_path(g2, 'A', 'C')
print(f"BFS (ignores weights): Distance = {bfs_dist}, Path = {bfs_path}")
print(f"Dijkstra (considers weights): Distance = {dijkstra_dist}, Path = {dijkstra_path}")
print("BFS finds shorter path by edges, Dijkstra finds shorter path by weight\n")

print("=== NEGATIVE WEIGHTS - Why we need Bellman-Ford ===")

# Graph with negative weights
g3 = Graph(directed=True)
g3.add_edge('A', 'B', 4)
g3.add_edge('A', 'C', 2)
g3.add_edge('B', 'C', -3)
g3.add_edge('C', 'D', 2)
g3.add_edge('B', 'D', 4)

dijkstra_dist, dijkstra_path = dijkstra_shortest_path(g3, 'A', 'D')
distances, predecessors, has_neg_cycle = bellman_ford_shortest_path(g3, 'A')
bf_path = reconstruct_path(predecessors, 'A', 'D')

print(f"Dijkstra (incorrect with negative weights): Distance = {dijkstra_dist}, Path = {dijkstra_path}")
print(f"Bellman-Ford: Distance = {distances['D']}, Path = {bf_path}")
print(f"Has negative cycle: {has_neg_cycle}")
print("Dijkstra gives suboptimal result due to negative weight\n")



