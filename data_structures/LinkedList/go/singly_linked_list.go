package main

// Package fmt is imported to use formatted I/O functions
import "fmt"

/*
	Node is a fundamental unit of data structure.
	Contains data and also may link to other nodes
*/
type Node struct {
	data int   // data of the node
	next *Node // pointer to the next node (it is nil if there is no next node)
}

/*
	LinkedList represents a concatenation of nodes
	It contains a head pointer to the first node in the list and a length attribute
*/
type LinkedList struct {
	head   *Node
	length int
}

/*
	Add adds a new node with the given data to the end of the list
	Time Complexity: O(n) - because we may need to traverse the entire list to find the end
	Space Complexity: O(1) - because we are only using a constant amount of extra space
*/
func (ll *LinkedList) Add(data int) {
	// Increment the length of the list
	ll.length++

	// Create a new node
	newNode := &Node{data: data}
	// If the LinkedList is empty, set the new node as the head
	if ll.head == nil {
		ll.head = newNode
		return
	}
	// Otherwise, traverse to the end of the list and add the new node
	current := ll.head
	for current.next != nil {
		current = current.next
	}
	current.next = newNode
}

/*
	Prepend adds a new node with the given data to the beginning of the list
	Time Complexity: O(1) - because we are adding the node at the beginning
	Space Complexity: O(1) - because we are only using a constant amount of extra space
*/
func (ll *LinkedList) Prepend(data int) {
	// Create a new node
	newNode := &Node{data: data}
	// Set the new node's next to the current head
	// and update the head to the new node
	newNode.next = ll.head
	ll.head = newNode
	// Increment the length of the list
	ll.length++
}

/*
	Display prints the linked list
	Time Complexity: O(n) - because we need to traverse the entire list to print it
*/
func (ll *LinkedList) Display() {
	// Set local variable current to the head of the list
	current := ll.head
	// Traverse the list and print each node's data
	for current != nil {
		fmt.Printf("%d -> ", current.data)
		current = current.next
	}
	// Print nil at the end to indicate the end of the list
	fmt.Println("nil")
}

// main function to demonstrate the linked list operations
func main() {
	ll := &LinkedList{}
	ll.Add(10)    // 10 -> nil
	ll.Add(20)    // 10 -> 20 -> nil
	ll.Prepend(5) // 5 -> 10 -> 20 -> nil
	ll.Display()  // Output: 5 -> 10 -> 20 -> nil
}
