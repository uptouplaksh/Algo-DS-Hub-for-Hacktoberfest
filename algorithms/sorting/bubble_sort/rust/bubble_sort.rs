use std::io;

/*
 * Bubble Sort Implementation in Rust
 *
 * Time Complexity: O(n^2)
 * Space Complexity: O(1)
 */

/// Bubble Sort function
/// Sorts a mutable slice in ascending order
fn bubble_sort<T: PartialOrd>(arr: &mut [T]) {
    let n = arr.len();
    // Traverse through all array elements
    for i in 0..n {
        // Last i elements are already in place
        for j in 0..(n - i - 1) {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1); // Swap if the element found is greater than next
            }
        }
    }
}

fn main() {
    println!("Enter numbers separated by spaces:");

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read input");

    // Parse input into a vector of integers
    let mut numbers: Vec<i32> = input
        .trim()
        .split_whitespace()
        .map(|x| x.parse::<i32>().expect("Invalid number"))
        .collect();

    println!("Before sorting: {:?}", numbers);
    bubble_sort(&mut numbers);
    println!("After sorting:  {:?}", numbers);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_empty_array() {
        let mut arr: [i32; 0] = [];
        bubble_sort(&mut arr);
        assert_eq!(arr, []);
    }

    #[test]
    fn test_sorted_array() {
        let mut arr = [1, 2, 3, 4, 5];
        bubble_sort(&mut arr);
        assert_eq!(arr, [1, 2, 3, 4, 5]);
    }

    #[test]
    fn test_unsorted_array() {
        let mut arr = [5, 3, 4, 1, 2];
        bubble_sort(&mut arr);
        assert_eq!(arr, [1, 2, 3, 4, 5]);
    }

    #[test]
    fn test_duplicates() {
        let mut arr = [3, 1, 2, 3, 2];
        bubble_sort(&mut arr);
        assert_eq!(arr, [1, 2, 2, 3, 3]);
    }

    #[test]
    fn test_negative_numbers() {
        let mut arr = [0, -1, 3, -2, 2];
        bubble_sort(&mut arr);
        assert_eq!(arr, [-2, -1, 0, 2, 3]);
    }
}
