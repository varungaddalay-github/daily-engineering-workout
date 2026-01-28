from collections import deque

class Graph:
    def __init__(self, n, directed=False):
        self.n = n
        self.adj_matrix = [[0]* n for _ in range(n)] # Space: n*n -> O(n^2)
        self.directed = directed

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        if not self.directed:
            self.adj_matrix[v][u] = 1

    def create_adj_matrix(self, edges):
        for u, v in edges:
            self.add_edge(u, v)
        

    def __str__(self):
        lines = []
        for row in self.adj_matrix:
            lines.append(" ".join(map(str, row)))
        return "\n".join(lines)
    
    def bfs_graph(self, start):
        res = []
        q = deque([start])
        visited = {start}

        while q:
            curr = q.popleft()
            res.append(curr)

            # neighbors are all columns where adj_matrix[curr][j] == 1
            for nbr in range(self.n):
                if self.adj_matrix[curr][nbr] == 1 and nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        
        return res


    
if __name__ == "__main__":
    edges = [[0,1], [0,2], [1,2], [2,3]]
    n = 4
    
    g = Graph(n)  
    g.create_adj_matrix(edges)

    print(g)
    print(g.bfs_graph(0))

