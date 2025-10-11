// // <<<< Maximum Profit in Job Scheduling >>>>

// /* You are given n jobs, where every job is represented by:
//    i. startTime[i]: the start time of the job.
//    ii. endTime[i]: the end time of the job.
//    iii. profit[i]: the profit you earn by completing the job.
//    Two jobs cannot be taken that overlap in time.
//    Return the maximum profit you can earn such that there are no two overlapping jobs in your selected subset.
   
//    Note: A job ending at time X is allowed to overlap with another job that starts exactly at time X. */



// // <<<< Solution >>>>

// /**
//  * This implementation uses a combination of dynamic programming with memoization
//  * and binary search for an efficient O(N log N) solution.
//  */

package data_structures.DynamicProgramming;
import java.util.Arrays;
import java.util.Comparator;

public class JobScheduling {

    static class Job {
        int s, e, p;
        Job(int s, int e, int p) { this.s = s; this.e = e; this.p = p; }
    }

    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        Job[] jobs = new Job[n];
        for (int i = 0; i < n; i++) jobs[i] = new Job(startTime[i], endTime[i], profit[i]);

        // Sort jobs by start time so we can binary-search the next non-overlapping job
        Arrays.sort(jobs, Comparator.comparingInt(j -> j.s));

        // Extract the start times into a separate array to perform binary search on
        int[] starts = new int[n];
        for (int i = 0; i < n; i++) starts[i] = jobs[i].s;

        // dp[i] will store the maximum profit obtainable considering jobs[i..n-1]
        // We use an extra space dp[n] = 0 as the base case (no jobs left => 0 profit)
        int[] dp = new int[n + 1];

        // Process jobs from the end to the beginning so that when computing dp[i]
        // the values dp[i+1] and dp[next] (for next > i) are already known.
        for (int i = n - 1; i >= 0; i--) {
            // Find the index of the first job whose start time is >= current job's end time
            // (i.e., the next job that does not overlap and can be taken after current job)
            int next = findNextJob(starts, jobs[i].e);

            // Choice 1: take the current job -> profit = jobs[i].p + dp[next]
            // Choice 2: skip the current job -> profit = dp[i + 1]
            // Take the better of the two choices.
            dp[i] = Math.max(jobs[i].p + dp[next], dp[i + 1]);
        }

        // dp[0] is the answer considering all jobs
        return dp[0];
    }

    private int findNextJob(int[] arr, int target) {
        int l = 0, r = arr.length - 1, ans = arr.length;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (arr[m] >= target) { ans = m; r = m - 1; } else l = m + 1;
        }
        return ans;
    }

    /*
     * Time & Space Complexity
     * -------------------------
     * Time Complexity:
     * - Sorting jobs by start time: O(n log n)
     * - Building `starts` array: O(n)
     * - The main DP loop runs n iterations and each iteration does a binary search
     *   (findNextJob) which takes O(log n), so this part is O(n log n).
     * Overall: O(n log n)
     *
     * Space Complexity:
     * - The `jobs` array stores n Job objects: O(n)
     * - The `starts` array: O(n)
     * - The `dp` array: O(n)
     * Overall auxiliary space: O(n)
     */

    public static void main(String[] args) {
        JobScheduling js = new JobScheduling();
        int[] start = {1, 2, 3};
        int[] end   = {3, 4, 5};
        int[] prof  = {50, 10, 40};
        System.out.println("Maximum Profit = " + js.jobScheduling(start, end, prof));
    }
}
