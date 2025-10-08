"""
Tower of Hanoi Puzzle Implementation in Python

Description:
This module demonstrates the classic Tower of Hanoi problem using recursion.
The objective is to move the entire stack to another rod, obeying a set of simple rules:

Time Complexity: O(2^n)
Space Complexity: O(n)

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
