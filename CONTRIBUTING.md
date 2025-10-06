## Our Contribution Process (Please Read!)

To ensure a fair and organized process for everyone, we follow a "First-Come, First-Served" system.

1.  **Claim an Issue:** Find an issue you want to work on and leave a comment asking to be assigned (e.g., "I'll take this one!" or "Please assign this to me").
2.  **Wait for Assignment:** Please wait for a maintainer to assign the issue to you before you start working. This prevents multiple people from working on the same thing. We will assign it to the first person who commented.
3.  **Submit a Pull Request:** Once you are assigned, you have **3 days** to submit a pull request. If there's no activity after 3 days, the issue will be un-assigned and become available for someone else to claim.
4.  **Link Your PR:** When you create your pull request, please link it to the issue you are solving.

Pull requests submitted for issues that were not claimed or were assigned to someone else will be closed.

## Step-by-Step Contribution Workflow

1.  **Find an Issue: ** Please look through the existing issues and find one you'd like to work on. If you have a new idea, feel free to open a new issue first. Comment on the issue to let us know you're working on it!

2.  **Fork the Repository:** Click the "Fork" button in the top-right corner of the page. This creates a copy of the repository in your own GitHub account.

3.  **Clone Your Fork:** Open your terminal and clone your forked repository:
    ```bash
    git clone [https://github.com/YOUR-USERNAME/Algo-DS-Hub-for-Hacktoberfest.git](https://github.com/YOUR-USERNAME/Algo-DS-Hub-for-Hacktoberfest.git)
    ```

4.  **Create a New Branch:** A dedicated branch for your feature is essential.
    ```bash
    git checkout -b your-branch-name
    # Example: git checkout -b add-python-binary-search
    ```

5.  **Add Your Code:**
    * Navigate to the correct directory based on our folder structure.
    * Create your file (e.g., `binary_search.py`).
    * Write your code. **Remember to add comments explaining the logic and the Time & Space Complexity.**

6.  **Commit Your Changes:** Make a clear and descriptive commit message.
    ```bash
    git add.
    git commit -m "feat: Add Binary Search algorithm in Python"
    ```

7.  **Push to Your Fork:** Push your changes to your forked repository.
    ```bash
    git push origin your-branch-name
    ```

8.  **Open a Pull Request (PR):**
    * Go to the original repository on GitHub.
    * You will see a prompt to create a Pull Request from your new branch. Click it.
    * Use a clear title (e.g., "Feat: Add Binary Search in Python").
    * In the description, link to the issue you are solving by writing `Closes #issue-number`.
    * Submit the PR!

Thank you for your contribution! We will review it as soon as possible.
