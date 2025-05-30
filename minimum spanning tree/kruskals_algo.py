'''
Kruskals algorithm to find the minimum spanning tree
'''

class DisjointSet:
    def __init__(self,size):
        self.parent=[i for i in range(size)]
        self.rank=[0]*size
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        if root_x==root_y:
            return None
        if self.rank[root_x]< self.rank[root_y]:
            self.parent[root_x]=root_y
        elif self.rank[root_x]> self.rank[root_y]:
            self.parent[root_y]=root_x
        else:
            self.parent[root_y]=root_x
            self.rank[root_x]+=1
        return True
    
    def connected(self,x,y):
        return self.find(x)==self.find(y)
    

'''
graph in the form (w,u,v)
[(1,0,1),(2,0,2)]
'''
def kruskal_mst(edge_list):
    ds=DisjointSet(6)
    edge_list.sort()
    mst_weight=0
    mst_edges=[]
    for w,u,v in edge_list:
        if ds.union(u,v):
            mst_weight+=w
            mst_edges.append((u,v,w))

    return mst_weight,mst_edges


edge_list = [
    (1, 0, 1),
    (3, 0, 2),
    (2, 1, 2),
    (4, 1, 3),
    (5, 2, 4),
    (6, 3, 4)
]

mst_weight,mst_edges=kruskal_mst(edge_list)
print(f'total MST weight = {mst_weight}')
for u,v,w in mst_edges:
    print(f"{u}-->{v}=={w}")