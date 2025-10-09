#include <iostream>
#include <vector>
using namespace std;

// This runs and compiles using:

// g++ -std=c++17 fenwick_tree.cpp -o fenwick_tree
// ./fenwick_tree

/*
    Fenwick Tree (Binary Indexed Tree)
    op:
    - update(i, delta): add delta at index i
    - query(i): prefix sum [1..i]
    - rangeQuery(l, r): sum [l..r]

    time com:  O(log n) per update/query
    Space comp: O(n)
*/
class FenwickTree 
{
    vector<int> bit; // 1-based
    int n;
    public:
    explicit FenwickTree(int n) : bit(n + 1, 0), n(n + 1){}

    void update(int i, int delta) 
    {
        for(; i < n; i += (i & -i)) bit[i] += delta;
    }
    int query(int i) const 
    {
        int sum = 0;
        for(; i > 0; i -= (i & -i)) sum += bit[i];
        return sum;
    }
    int rangeQuery(int l, int r) const{return query(r) - query(l - 1);}
};

int main() 
{
    int n = 10;
    FenwickTree ft(n);

    // 1-based array (arr[0] unused)
    vector<int> arr = {0, 3, 2, -1, 6, 5, 4, -3, 3, 7, 2};

    for(int i = 1; i <= n; ++i) ft.update(i, arr[i]);

    cout << "Prefix sum up to index 5: " << ft.query(5) << '\n'; // 15
    cout << "Range sum [3, 8]: " << ft.rangeQuery(3, 8) << '\n'; // 14

    ft.update(4, 5); // add +5 at index 4 (6 -> 11)
    cout << "After updating index 4 by +5, prefix sum up to 5: " << ft.query(5) << '\n'; // 20
    
    return 0;
}
