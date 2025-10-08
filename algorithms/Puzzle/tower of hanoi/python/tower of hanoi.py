"""
Tower of Hanoi Puzzle Implementation in Python

Description:
This module demonstrates the classic Tower of Hanoi problem using recursion.
The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks.
The objective is to move the entire stack to another rod, obeying the following rules:
    1. Only one disk can be moved at a time.
    2. Each move involves taking the upper disk from one stack and placing it on another rod.
    3. No larger disk may be placed on top of a smaller disk.

File Location:
algorithms/puzzles/tower_of_hanoi/python/tower_of_hanoi.py
Solve the Tower of Hanoi problem recursively.

Parameters:
n (int): Number of disks
source (str): The rod from which to move disks initially
auxiliary (str): The rod used as a helper
destination (str): The rod to move all disks to

Prints:
Steps to move each disk from source to destination rod.

Time Complexity: O(2^n)
    - Each disk move generates two recursive calls.
Space Complexity: O(n)
    - Due to the recursion call stack.
"""

def tower_of_hanoi(n, source, auxiliary, destination):

    # Base case: Only one disk to move
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return

    # Step 1: Move top n-1 disks from source to auxiliary using destination as helper
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Step 2: Move the nth (largest) disk from source to destination
    print(f"Move disk {n} from {source} → {destination}")

    # Step 3: Move the n-1 disks from auxiliary to destination using source as helper
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# ------------------------- RUNNABLE EXAMPLE -------------------------
if __name__ == "__main__":
    print("Tower of Hanoi Recursive Solution\n")

    # Example: Solve for 3 disks
    num_disks = 3
    print(f"Number of disks: {num_disks}\n")
    tower_of_hanoi(num_disks, source="A", auxiliary="B", destination="C")

    print("\nAll disks have been successfully moved!")
