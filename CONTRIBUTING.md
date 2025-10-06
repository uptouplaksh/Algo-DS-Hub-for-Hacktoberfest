# Contribution Guidelines

We are excited to have you contribute! This guide will walk you through the process.

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
