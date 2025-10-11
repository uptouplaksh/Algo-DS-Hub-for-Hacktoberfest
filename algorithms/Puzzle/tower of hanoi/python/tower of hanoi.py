"""
===========================================
   Tower of Hanoi Puzzle Implementation
===========================================

📘 Description:
This Python program demonstrates the classic Tower of Hanoi problem 
using a recursive approach.

The objective is to move all disks from the source rod to the 
destination rod using the auxiliary rod, following these rules:

1️⃣ Only one disk can be moved at a time.  
2️⃣ Each move consists of taking the upper disk from one rod 
    and placing it on top of another rod.  
3️⃣ No disk may be placed on top of a smaller disk.

🧮 Time Complexity: O(2^n)
💾 Space Complexity: O(n)
"""

def tower_of_hanoi(num_disks, source, auxiliary, destination):
    """
    Solves the Tower of Hanoi problem using recursion.

    Args:
        num_disks (int): Number of disks to move.
        source (str): The starting rod.
        auxiliary (str): The helper rod.
        destination (str): The target rod.
    """

    # Base case: Only one disk to move
    if num_disks == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return

    # Step 1: Move top n-1 disks from source → auxiliary
    tower_of_hanoi(num_disks - 1, source, destination, auxiliary)

    # Step 2: Move the nth (largest) disk from source → destination
    print(f"Move disk {num_disks} from {source} → {destination}")

    # Step 3: Move the n-1 disks from auxiliary → destination
    tower_of_hanoi(num_disks - 1, auxiliary, source, destination)


# ------------------------- RUNNABLE EXAMPLE -------------------------
if __name__ == "__main__":
    print("🔹 Tower of Hanoi — Recursive Solution 🔹\n")

    num_disks = 3  # Example with 3 disks (you can change this)
    print(f"Number of disks: {num_disks}\n")

    tower_of_hanoi(num_disks, source="A", auxiliary="B", destination="C")

    print("\n✅ All disks have been successfully moved!")
