import java.util.Scanner;

/**
 * Stack implementation in Java using array.
 *
 * Operations supported:
 * 1. Push
 * 2. Pop
 * 3. Peek
 * 4. Display
 *
 * Time Complexity:
 * Push, Pop, Peek: O(1)
 * Display: O(n)
 *
 * Space Complexity: O(n)
 */
public class stack {
    private int maxSize;
    private int[] stackArray;
    private int top;

    // Constructor to initialize stack
    public stack(int size) {
        maxSize = size;
        stackArray = new int[maxSize];
        top = -1;
    }

    // Push element onto stack
    public void push(int value) {
        if (top >= maxSize - 1) {
            System.out.println("Stack Overflow!");
        } else {
            stackArray[++top] = value;
            System.out.println(value + " pushed onto stack.");
        }
    }

    // Pop element from stack
    public void pop() {
        if (top < 0) {
            System.out.println("Stack Underflow!");
        } else {
            int value = stackArray[top--];
            System.out.println(value + " popped from stack.");
        }
    }

    // Peek top element
    public void peek() {
        if (top < 0) {
            System.out.println("Stack is empty!");
        } else {
            System.out.println("Top element is " + stackArray[top]);
        }
    }

    // Display stack elements
    public void display() {
        if (top < 0) {
            System.out.println("Stack is empty!");
        } else {
            System.out.println("Stack elements:");
            for (int i = top; i >= 0; i--) {
                System.out.println(stackArray[i]);
            }
        }
    }

    // Main method for dynamic input
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter stack size: ");
        int size = sc.nextInt();
        stack stack = new stack(size);

        while (true) {
            System.out.println("\nChoose operation: 1-Push 2-Pop 3-Peek 4-Display 5-Exit");
            int choice = sc.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter value to push: ");
                    int value = sc.nextInt();
                    stack.push(value);
                    break;
                case 2:
                    stack.pop();
                    break;
                case 3:
                    stack.peek();
                    break;
                case 4:
                    stack.display();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    sc.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}
