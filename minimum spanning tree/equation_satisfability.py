'''
satisfiability of equations
'''

class DisjointSet:
    def __init__(self,size):
        self.parent=list(range(size))
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
    
class Solution:
    def is_equation_possible(self,equation_list):
        ds=DisjointSet(26)
        for equation in equation_list:
            if equation[1:3]=="==":
                x=ord(equation[:1])-ord('a')
                y=ord(equation[3:])-ord('a')
                ds.union(x,y)
        for equation in equation_list:
            if equation[1:3]=="!=":
                x=ord(equation[:1])-ord('a')
                y=ord(equation[3:])-ord('a')
                if ds.find(x)==ds.find(y):
                    return False
        return True
    
s = Solution()
print(s.is_equation_possible(["a==b", "b!=a"]))     # False
print(s.is_equation_possible(["a==b", "b==c", "a==c"])) # True
print(s.is_equation_possible(["c==c", "b==d", "x!=z"])) # True
print(s.is_equation_possible(["c==c", "b==d", "x!=z","d==g","g==p","p==c","c!=g"])) # False