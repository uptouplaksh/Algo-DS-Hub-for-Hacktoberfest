# Author: vaishnavijha12
# Problem: Minimum Cost to Connect All Points
# Approach: Kruskal’s Algorithm with Union-Find
# Time Complexity: O(E log E)
# Space Complexity: O(V)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[py] = px
        return True

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges.sort()

        uf = UnionFind(n)
        cost, count = 0, 0
        for d, u, v in edges:
            if uf.union(u, v):
                cost += d
                count += 1
                if count == n - 1:
                    break
        return cost

# ---------- Test Code ----------
if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    solution = Solution()
    print("Minimum Cost to Connect All Points:", solution.minCostConnectPoints(points))
