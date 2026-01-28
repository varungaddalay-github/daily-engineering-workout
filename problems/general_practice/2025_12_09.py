from collections import defaultdict, deque
import heapq

"""
Weighted Graphs
- Edges with weights attached to them

edges = [
    (0, 1, 2),
    (0, 2, 5),
    (1, 2, 1),
    (2, 3, 2)
    ]
    
"""

class WeightedGraph:
    def __init__(self, directed=False):
        self.adj_lst = defaultdict(list)
        self.directed = directed

    def create_adj_list(self, edges):
        for u, v, w in edges:
            self.adj_lst[u].append((v, w))
            if not self.directed:
                self.adj_lst[v].append((u, w))

    def __str__(self):
        return str(self.adj_lst)
    
    # -----------------------------------------------------
    # 1️⃣ BFS-STYLE TRAVERSAL (weights ignored)
    # -----------------------------------------------------

    def bfs_weighted_traversal(self, start):
        res = []
        q = deque([start])
        visited = {start}

        while q:
            curr = q.popleft()
            res.append(curr)
            for neighbor, w in self.adj_lst[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return res
    
    # -----------------------------------------------------
    # 2️⃣ DIJKSTRA = WEIGHTED BFS (min-heap)
    # -----------------------------------------------------

    def bfs_weighted_shortest_path(self, start):
        """
        Computes shortest paths from start node using Weighted BFS (Dijkstra).
        Returns a dictionary of node -> min distance.

        - For weighted graphs with arbitrary positive weights, 
        we use Dijkstra’s Algorithm (which is still BFS-shaped but uses a min-heap priority queue, 
        not a normal queue).

        """
        min_dist = {node: float('inf') for node in self.adj_lst}
        min_dist[start] = 0

        # priority queue stores: (distance_so_far, node)
        pq = [(0, start)]

        while pq:
            curr_dist, node = heapq.heappop(pq)

            if curr_dist > min_dist[node]:
                continue

            for nbr, w in self.adj_lst[node]:
                new_dist = curr_dist + w
                if new_dist < min_dist[nbr]:
                    min_dist[nbr] = new_dist
                    heapq.heappush(pq, (new_dist, nbr))

        return min_dist

    

if __name__ == "__main__":
    wg = WeightedGraph()
    edges = [(0, 1, 2), (0, 2, 5), (1, 2, 1), (2, 3, 2)]
    wg.create_adj_list(edges)
    print(wg)
    print(wg.bfs_weighted_traversal(0))
    print(wg.bfs_weighted_shortest_path(0))


