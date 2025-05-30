'''
disjoint set implementation
'''

class DisjointSet:
    def __init__(self,size):
        self.parent=[i for i in range(size)]
        self.rank = [0]* size

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

    def connected(self,x,y):
        return self.find(x)==self.find(y)
    
ds = DisjointSet(10)

ds.union(1, 2)
ds.union(2, 3)

print(ds.connected(1, 3))  # True
print(ds.connected(1, 4))  # False

ds.union(4, 5)
ds.union(3, 4)

print(ds.connected(1, 5))  # True