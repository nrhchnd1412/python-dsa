'''
You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
where the second project is dependent on the first project). All of a project's dependencies must be
built before the project is. Find a build order that will allow the projects to be built.
If there is no valid build order, return an error.
'''

from collections import defaultdict, deque


def build_project_graph(project_list,dependencies_list):
    projects=defaultdict(list)
    for dependency,project in dependencies_list:
        projects[dependency].append(project)
    for project in project_list:
        projects[project]
    return projects

def find_build_order(projects, dependencies):
    project_graph=build_project_graph(projects,dependencies)
    visited={j: False for j in projects}
    stack=[]

    def dfs(visited,stack,node):
        visited[node]=True
        for neighbour in project_graph[node]:
            if not visited[neighbour]:
                dfs(visited,stack,neighbour)
        stack.append(node)

    for v in projects:
        if not visited[v]:
            dfs(visited,stack,v)
    
    print(stack[::-1])

def kahns_topological_sort(projects,dependencies):
    project_graph=defaultdict(list)
    in_degree={p:0 for p in projects}
    for deps,project in dependencies:
        project_graph[deps].append(project)
        in_degree[project]+=1
    
    q=deque([i for i in in_degree if in_degree[i]==0])
    order = []
    while q:
        item = q.popleft()
        order.append(item)
        for neighbour in project_graph[item]:
            in_degree[neighbour]-=1
            if in_degree[neighbour]==0:
                q.append(neighbour)
    if len(order)!=len(projects):
        print("Cycle detected")
        return None
    return "->".join(map(str,order))
    

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]
find_build_order(projects,dependencies)
print(kahns_topological_sort(projects,dependencies))
# output
#['f', 'e', 'b', 'a', 'd', 'c']