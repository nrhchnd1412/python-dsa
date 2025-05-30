'''
Prims algorithm
'''
import heapq

def prim(graph,start=0):
    total_weight=0
    prim_edges=[]
    visited=set()
    adj_list = [(0,start,-1)]
    while adj_list and len(visited)<len(graph):
        w,u,parent=heapq.heappop(adj_list)
        if u in visited:
            continue
        visited.add(u)
        total_weight+=w
        if parent!=-1:
            prim_edges.append((parent,u,w))
        for v,w in graph[u]:
            if v not in visited:
                heapq.heappush(adj_list,(w,v,u))
    return total_weight,prim_edges
    
graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)],
    5: [(1, 6)],
}

weight, mst = prim(graph)
print("Total weight of MST:", weight)
print("Edges in MST:", mst)