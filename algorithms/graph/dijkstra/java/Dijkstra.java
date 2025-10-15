import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

/**
 * Dijkstra's Algorithm (Optimized with Priority Queue)
 *
 * Description:
 * Implements Dijkstra's algorithm to find the shortest paths from a source node to all other nodes in a weighted graph using an adjacency list and a priority queue.
 *
 * Time Complexity: O((V + E) log V) where V is the number of vertices and E is the number of edges.
 * Space Complexity: O(V + E) for the adjacency list, distance array, and priority queue.
 */
public class Dijkstra {

    static class Pair implements Comparable<Pair> {
        int vertex;
        int weight;

        public Pair(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }

        @Override
        public int compareTo(Pair other) {
            return this.weight - other.weight;
        }
    }

    public static int[] dijkstra(int V, ArrayList<ArrayList<Pair>> adj, int S) {

        int[] dist = new int[V];
        Arrays.fill(dist, Integer.MAX_VALUE);

        dist[S] = 0;

        // A Priority Queue (min-heap) to store {vertex, distance} pairs.
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        pq.add(new Pair(S, 0));

        while (!pq.isEmpty()) {
            Pair current = pq.poll();
            int u = current.vertex;
            int d = current.weight;

            if (d > dist[u]) {
                continue;
            }

            for (Pair edge : adj.get(u)) {
                int v = edge.vertex;
                int edgeWeight = edge.weight;

                if (dist[u] != Integer.MAX_VALUE && dist[u] + edgeWeight < dist[v]) {
                    dist[v] = dist[u] + edgeWeight;
                    pq.add(new Pair(v, dist[v]));
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {

        /*
         * Example Input:
         * V = 5, E = 6
         * Edges: (u, v, w)
         * 0 1 2
         * 0 2 4
         * 1 2 1
         * 1 3 7
         * 2 4 3
         * 3 4 1
         * Source: 0
         *
         * Expected Output:
         * Shortest distances from node 0: [0, 2, 3, 9, 6]
         */

        int V = 5;
        int source = 0;

        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }

        adj.get(0).add(new Pair(1, 2));
        adj.get(0).add(new Pair(2, 4));
        adj.get(1).add(new Pair(2, 1));
        adj.get(1).add(new Pair(3, 7));
        adj.get(2).add(new Pair(4, 3));
        adj.get(3).add(new Pair(4, 1));

        int[] distances = dijkstra(V, adj, source);

        System.out.println("Shortest distances from node " + source + ": " + Arrays.toString(distances));
    }
}