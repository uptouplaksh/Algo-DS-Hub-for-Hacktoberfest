import java.util.Arrays;

/**
 * Job Sequencing with Deadlines - Greedy Algorithm
 *
 * Problem:
 * Given a set of jobs where each job has a deadline and profit,
 * schedule the jobs to maximize total profit, assuming each job
 * takes 1 unit of time.
 *
 * Approach:
 * 1. Sort all jobs in decreasing order of profit.
 * 2. Allocate each job to the latest available slot before its deadline.
 * 3. Keep track of which slots are occupied.
 *
 * Time Complexity: O(n^2)
 * Space Complexity: O(n)
 *
 * Example:
 * Input:
 * Jobs = [(id=A, deadline=2, profit=100),
 *          (id=B, deadline=1, profit=19),
 *          (id=C, deadline=2, profit=27),
 *          (id=D, deadline=1, profit=25),
 *          (id=E, deadline=3, profit=15)]
 *
 * Output:
 * Maximum Profit = 142
 * Job Sequence: C, A, E
 */

public class Job_Sequencing {

    // Job class to store job details
    static class Job {
        char id;       // Job ID (A, B, C, ...)
        int deadline;  // Job deadline
        int profit;    // Job profit

        public Job(char id, int deadline, int profit) {
            this.id = id;
            this.deadline = deadline;
            this.profit = profit;
        }
    }

    /**
     * Function to find the maximum profit sequence of jobs.
     */
    static void jobSequencing(Job[] jobs) {
        int n = jobs.length;

        // Step 1: Sort jobs in descending order of profit
        Arrays.sort(jobs, (a, b) -> b.profit - a.profit);

        // Step 2: Find the maximum deadline to determine number of time slots
        int maxDeadline = 0;
        for (Job job : jobs) {
            maxDeadline = Math.max(maxDeadline, job.deadline);
        }

        // Step 3: Create time slots (1-based indexing for clarity)
        char[] jobSequence = new char[maxDeadline];
        boolean[] slotFilled = new boolean[maxDeadline];

        int totalProfit = 0;

        // Step 4: Iterate through jobs and assign to available slots
        for (Job job : jobs) {
            // Try to find a slot from job.deadline - 1 to 0
            for (int j = job.deadline - 1; j >= 0; j--) {
                if (!slotFilled[j]) {
                    slotFilled[j] = true;
                    jobSequence[j] = job.id;
                    totalProfit += job.profit;
                    break;
                }
            }
        }

        // Step 5: Display results
        System.out.print("Selected Job Sequence: ");
        for (int i = 0; i < maxDeadline; i++) {
            if (slotFilled[i]) {
                System.out.print(jobSequence[i] + " ");
            }
        }
        System.out.println("\nMaximum Profit: " + totalProfit);
    }

    // Main method for demonstration
    public static void main(String[] args) {
        Job[] jobs = {
                new Job('A', 2, 100),
                new Job('B', 1, 19),
                new Job('C', 2, 27),
                new Job('D', 1, 25),
                new Job('E', 3, 15)
        };

        jobSequencing(jobs);
    }
}
