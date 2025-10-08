# Data Structures

## 📚 What are Data Structures?

Data structures are specialized formats for organizing, processing, storing, and retrieving data efficiently. They provide a means to manage large amounts of data effectively for various use cases such as databases, internet indexing services, and more.

A well-chosen data structure can dramatically improve the performance of a program by optimizing operations like insertion, deletion, searching, and sorting. Understanding data structures is fundamental to computer science and is essential for writing efficient, scalable code and solving complex algorithmic problems.

## 🗂️ Available Data Structures

This folder contains implementations of the following data structures in multiple programming languages:

### **Linked List** (`Linked_List/`)

A linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.

**Implementations:**

- **Python** (`python/`)
  - `singly_linked_list.py` - Basic singly linked list implementation
  - `interactive_demo.py` - Interactive demonstration of linked list operations

**Common Operations:**

- Insertion (at beginning, end, or specific position)
- Deletion (by value or position)
- Traversal
- Search

**Time Complexity:**

- Access: O(n)
- Search: O(n)
- Insertion: O(1) at head, O(n) at tail
- Deletion: O(1) at head, O(n) at tail

---

### **Stack** (`Stack/`)

A linear data structure that follows the LIFO (Last In First Out) principle, where the last element added is the first one to be removed.

**Implementations:**

- **C** (`C/`)
- **Python** (`python/`)

**Common Operations:**

- Push - Add element to top
- Pop - Remove element from top
- Peek/Top - View top element without removing
- isEmpty - Check if stack is empty

**Time Complexity:**

- Push: O(1)
- Pop: O(1)
- Peek: O(1)

**Use Cases:**

- Function call management (call stack)
- Expression evaluation and parsing
- Backtracking algorithms
- Undo/Redo functionality

---

## 🤝 How to Contribute a New Data Structure

We welcome contributions from developers of all skill levels! Follow these steps to add a new data structure implementation:

### **Step 1: Check Existing Implementations**

Before starting, verify that the data structure isn't already implemented. Some popular data structures you can contribute:

- Queue (FIFO structure)
- Binary Tree
- Binary Search Tree
- AVL Tree
- Hash Table
- Graph
- Heap (Min Heap, Max Heap)
- Trie
- Doubly Linked List
- Circular Linked List
- Priority Queue
- Deque (Double-ended Queue)

### **Step 2: Understand the Folder Structure**

All data structures **MUST** follow this exact structure:

```
data_structures/
├── YourDataStructure/
│   ├── python/
│   │   └── your_data_structure.py
│   ├── javascript/
│   │   └── YourDataStructure.js
│   ├── c_plus_plus/
│   │   └── your_data_structure.cpp
│   └── README.md (optional but recommended)
```

**Naming Conventions:**

- **Folder names:** Use PascalCase (e.g., `BinaryTree`, `HashTable`)
- **Language subfolders:** Use lowercase (e.g., `python`, `javascript`, `c_plus_plus`, `java`)
- **File names:**
  - Python: Use snake_case (e.g., `binary_tree.py`)
  - JavaScript: Use PascalCase (e.g., `BinaryTree.js`)
  - C++: Use snake_case (e.g., `binary_tree.cpp`)

### **Step 3: Implementation Requirements**

Your implementation **MUST** include:

✅ **Clean, well-documented code** with:

- Clear variable and function names
- Inline comments explaining complex logic
- Header comments explaining the purpose

✅ **Core operations** of the data structure:

- Creation/Initialization
- Insertion
- Deletion
- Search/Access
- Traversal (if applicable)
- Any structure-specific operations

✅ **Example usage** demonstrating:

- How to create an instance
- How to perform basic operations
- Expected output

✅ **Comments documenting:**

- Time complexity of each operation
- Space complexity
- Edge cases handled

### **Step 4: Code Quality Standards**

- Write clear, readable code that follows the language's conventions
- Use meaningful variable and function names
- Add docstrings (Python) or JSDoc comments (JavaScript)
- Handle edge cases (empty structure, null values, etc.)
- Avoid hardcoded values where possible
- Test your implementation thoroughly before submitting

### **Step 5: Submit Your Contribution**

1. **Fork the repository** to your GitHub account
2. **Clone your fork** to your local machine
3. **Create a new branch** for your data structure:
   ```bash
   git checkout -b add-<data-structure-name>
   ```
4. **Add your implementation** following the folder structure above
5. **Test your code** to ensure it works correctly
6. **Commit your changes** with a clear message:
   ```bash
   git add .
   git commit -m "feat: add <DataStructure> implementation in <language>"
   ```
7. **Push to your fork:**
   ```bash
   git push origin add-<data-structure-name>
   ```
8. **Create a Pull Request** on the original repository

### **Step 6: Pull Request Guidelines**

Your PR **MUST** include:

- A descriptive title: `feat: add [DataStructure] implementation in [Language]`
- A clear description of what you've implemented
- Reference to any related issue (e.g., `Closes #XX`)
- Confirmation that you've tested the code

**Note:** Pull requests that do not follow the folder structure and contribution guidelines will be marked as invalid and closed.

---

## 📖 Learning Resources

Enhance your understanding of data structures with these resources:

- 📚 [GeeksforGeeks - Data Structures](https://www.geeksforgeeks.org/data-structures/)
- 🎥 [VisuAlgo - Visualize Data Structures](https://visualgo.net/)
- 📊 [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- 📖 [Data Structures - Programiz](https://www.programiz.com/dsa)
- 🎓 [MIT OpenCourseWare - Introduction to Algorithms](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/)

---

## 📋 Quick Reference

### Time Complexity Comparison

| Data Structure | Access    | Search    | Insertion | Deletion  |
| -------------- | --------- | --------- | --------- | --------- |
| Array          | O(1)      | O(n)      | O(n)      | O(n)      |
| Linked List    | O(n)      | O(n)      | O(1)\*    | O(1)\*    |
| Stack          | O(n)      | O(n)      | O(1)      | O(1)      |
| Queue          | O(n)      | O(n)      | O(1)      | O(1)      |
| Hash Table     | N/A       | O(1)†     | O(1)†     | O(1)†     |
| Binary Tree    | O(n)      | O(n)      | O(n)      | O(n)      |
| BST            | O(log n)† | O(log n)† | O(log n)† | O(log n)† |

_\* At head; O(n) at tail for singly linked list_  
_† Average case; worst case O(n)_

---

## 🌟 Contributors

A huge thank you to all the contributors who have helped build this collection! Your efforts make this repository a valuable resource for the developer community.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

---

## 💬 Need Help?

If you have questions or need clarification on contributing:

1. Check the [CONTRIBUTING.md](../CONTRIBUTING.md) guide
2. Review existing implementations for reference
3. Open an issue with the `question` label
4. Join the discussion in existing issues

---

**Happy Coding! 🚀**

_Let's build a comprehensive, high-quality resource for learning data structures together!_
