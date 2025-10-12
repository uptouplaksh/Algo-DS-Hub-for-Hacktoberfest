package main

import "fmt"

// Node represents a node in a singly linked list
type Node struct {
	data int
	next *Node
}

// LinkedList represents a singly linked list
type LinkedList struct {
	head *Node
}

// Add adds a new node with the given data to the end of the list
func (ll *LinkedList) Add(data int) {
	newNode := &Node{data: data}
	if ll.head == nil {
		ll.head = newNode
		return
	}
	current := ll.head
	for current.next != nil {
		current = current.next
	}
	current.next = newNode
}

// Prepend adds a new node with the given data to the beginning of the list
func (ll *LinkedList) Prepend(data int) {
	newNode := &Node{data: data}
	newNode.next = ll.head
	ll.head = newNode
}

// Display prints the linked list
func (ll *LinkedList) Display() {
	current := ll.head
	for current != nil {
		fmt.Printf("%d -> ", current.data)
		current = current.next
	}
	fmt.Println("nil")
}

// main function to demonstrate the linked list operations
func main() {
	ll := &LinkedList{}
	ll.Add(10)
	ll.Add(20)
	ll.Prepend(5)
	ll.Display() // Output: 5 -> 10 -> 20 -> nil
}