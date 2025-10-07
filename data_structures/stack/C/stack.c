#include <stdio.h>
#include <stdlib.h>

#define max 10
int top = -1;
int stack[max];

void push();
void pop();
void isEmpty();
void isFull();
void peek();
void count();
void change();
void display();

void push() // Insert element at top
{
    if (top == max - 1)
    {
        printf("Stack overflow\n");
    }
    else
    {
        int val;
        printf("Enter value to be inserted: ");
        scanf("%d", &val);
        top += 1;
        stack[top] = val;
    }
}

void pop() // Remove element from top
{
    if (top == -1)
    {
        printf("Stack underflow\n");
    }
    else
    {
        printf("Popped element: %d\n", stack[top]);
        top -= 1;
    }
}

void isEmpty() // Check if stack is empty
{
    if (top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Stack is not empty\n");
    }
}

void isFull() // Check if stack is full
{
    if (top == max - 1)
    {
        printf("Stack is full\n");
    }
    else
    {
        printf("Stack is not full\n");
    }
}

void peek() // View top element
{
    if (top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Top element: %d\n", stack[top]);
    }
}

void count() // Count number of elements in stack
{
    printf("Number of elements in stack: %d\n", top + 1);
}

void change() // Change element at specific position
{
    int pos, newVal;
    printf("Enter position to change: ");
    scanf("%d", &pos);

    if (pos >= 0 && pos <= top)
    {
        printf("Enter new value: ");
        scanf("%d", &newVal);
        stack[pos] = newVal;
        printf("Value changed at position %d\n", pos);
    }
    else
    {
        printf("Invalid position\n");
    }
}

void display() // Display all stack elements
{
    if (top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Stack elements (top to bottom): ");
        for (int i = top; i >= 0; i--)
        {
            printf("%d ", stack[i]);
        }
        printf("\n");
    }
}

int main() // Main function with menu
{
    int ch;
    do
    {
        printf("\n1) Push\n2) Pop\n3) Peek\n4) Count\n5) Change\n6) Display\n7) Is full\n8) Is empty\n9) Exit\nEnter choice: ");
        scanf("%d", &ch);

        switch (ch)
        {
        case 1:
            push();
            break;

        case 2:
            pop();
            break;

        case 3:
            peek();
            break;

        case 4:
            count();
            break;

        case 5:
            change();
            break;

        case 6:
            display();
            break;

        case 7:
            isFull();
            break;

        case 8:
            isEmpty();
            break;
        case 9:
            exit(0);
            break;

        default:
            printf("Invalid choice\n");
            break;
        }
    } while (ch != 9);

    return 0;
}
