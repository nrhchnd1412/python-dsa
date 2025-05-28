'''
Floyd Warshall algorithm
'''

def floyd_warshall_with_path(graph):
    n = len(graph)
    distances = [row[:] for row in graph]
    next_node=[[None if graph[i][j] ==float("inf") else j for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k]!=float("inf") or distances[k][j]!=float("inf"):
                    if distances[i][k]+distances[k][j] < distances[i][j]:
                        distances[i][j]=distances[i][k]+distances[k][j]
                        next_node[i][j]=next_node[i][k]

    for i in range(n):
        if distances[i][i]<0:
            raise ValueError("Neagtive cycle detected")
        
    return distances,next_node

def reconstruct_path(u,v,next_node):
    if next_node[u][v] is None:
        return []
    path =[u]
    while u!=v:
        u=next_node[u][v]
        path.append(u)
    return " -> ".join(map(str,path))

graph = [
    [0,   3,   float('inf'), 5],
    [2,   0,   float('inf'), 4],
    [float('inf'), 1, 0,     float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

dist, next_node = floyd_warshall_with_path(graph)

print("Shortest distances:")
for row in dist:
    print(row)

print("\nShortest path from 0 to 2:")
path = reconstruct_path(0, 2, next_node)
print(path)