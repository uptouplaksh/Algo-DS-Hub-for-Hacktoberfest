"""
Time Complexity:
- find(x): O(α(n)) amortized, where α is the inverse Ackermann function (very slow-growing)
- union(x, y): O(α(n)) amortized, due to union by rank/size and path compression

Space Complexity: O(n)
- We maintain two lists of size n: `parent` and `rank` (or `size`)
"""

class UnionFind:


    def __init__(self, size):

        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):

        if self.parent[x] != x:
            # Recursively find the root and compress the path
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already connected

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


# 🧪 Runnable example block
def main():
    """
    Example usage of the UnionFind class.
    Demonstrates union and find operations and verifies connected components.
    """

    # Initialize UnionFind with 10 elements (0 through 9)
    uf = UnionFind(10)

    # Initially, each element is its own parent
    print("Initial parent list:")
    print(uf.parent)
    print("-" * 40)

    # Perform unions
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(6, 7)
    uf.union(5, 6)

    # Test connectivity
    print("After performing unions:")
    for i in range(8):
        print(f"find({i}) = {uf.find(i)}")

    print("-" * 40)
    print(f"Are 1 and 3 connected? {'Yes' if uf.find(1) == uf.find(3) else 'No'}")  # Yes
    print(f"Are 4 and 7 connected? {'Yes' if uf.find(4) == uf.find(7) else 'No'}")  # Yes
    print(f"Are 1 and 7 connected? {'Yes' if uf.find(1) == uf.find(7) else 'No'}")  # No

    # Try to union two already connected nodes
    print("-" * 40)
    result = uf.union(2, 3)
    print(f"Union of 2 and 3 performed? {'Yes' if result else 'No'}")  # No


if __name__ == "__main__":
    main()
