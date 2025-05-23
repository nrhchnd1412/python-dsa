class Graph:
    def __init__(self,gdict=None):
        if not gdict:
            self.gdict={}
        else:
            self.gdict=gdict
    
    def insert_node(self,node):
        self.gdict[node]=[]
    
    def insert_vertex(self,node1,node2):
        if node1 in self.gdict.keys() and node2 in self.gdict.keys():
            self.gdict[node1].append(node2)
            self.gdict[node2].append(node1)
            return True
        return False
    
    def delete_vertex(self,node1,node2):
        if node1 in self.gdict.keys() and node2 in self.gdict.keys():
            try:
                self.gdict[node1].remove(node2)
                self.gdict[node2].remove(node1)
                return True
            except ValueError:
                pass
        return False

    def delete_node(self,node):
        if node in self.gdict.keys():
            for edge in self.gdict[node]:
                self.gdict[edge].remove(node)
            del self.gdict[node]
            return True
        return False
    
    def __str__(self):
        return str(self.gdict)

gdict={
    "A":["B","C"],
    "B":["A","E"],
    "E":["B","D"],
    "D":["E","C"],
    "C":["A","D"]
}
g=Graph(gdict)
print(g)

g.insert("D","A")
print(g)