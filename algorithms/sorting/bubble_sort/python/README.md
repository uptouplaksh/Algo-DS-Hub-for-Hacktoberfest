# Bubble Sort

## 🔹 What is Bubble Sort?
Bubble Sort is a simple sorting algorithm that repeatedly compares **adjacent elements** in an array and **swaps them** if they are in the wrong order.  
This process continues until the entire array is sorted. The largest values "bubble up" to the end of the array, similar to bubbles rising in water.

---

## **Algorithm (Step by Step)**

1. Start from the first element of the array.  
2. Compare it with the next element.  
3. If the current element is greater than the next element, swap them.  
4. Move to the next pair of elements and repeat step 3 until the end of the array.  
5. After each pass, the largest element moves to its correct position.  
6. Repeat steps 1–5 for the remaining unsorted elements.  

---

## **Step-by-Step Example**

Array: `[5, 1, 4, 2, 8]`

**Pass 1:**  
- Compare 5 and 1 → swap → `[1, 5, 4, 2, 8]`  
- Compare 5 and 4 → swap → `[1, 4, 5, 2, 8]`  
- Compare 5 and 2 → swap → `[1, 4, 2, 5, 8]`  
- Compare 5 and 8 → no swap → `[1, 4, 2, 5, 8]`  

**Pass 2:**  
- Compare 1 and 4 → no swap  
- Compare 4 and 2 → swap → `[1, 2, 4, 5, 8]`  
- Compare 4 and 5 → no swap  
- Compare 5 and 8 → no swap  

**Pass 3:**  
- Compare 1 and 2 → no swap  
- Compare 2 and 4 → no swap  
- Compare 4 and 5 → no swap  
- Compare 5 and 8 → no swap  

**Pass 4:**  
- Compare 1 and 2 → no swap  
- Compare 2 and 4 → no swap  
- Compare 4 and 5 → no swap  

✅ Array is now sorted: `[1, 2, 4, 5, 8]`

---

## **Optimized Bubble Sort (Best Case Handling)**

To handle already sorted arrays efficiently, we can use a **swapped flag**:

- Start each pass with `swapped = false`.  
- If a swap occurs during the pass, set `swapped = true`.  
- If no swaps occur (`swapped = false`), the array is already sorted → **stop early**.

**Pseudocode:**

```text
for i from 0 to n-1
    swapped = false
    for j from 0 to n-i-2
        if array[j] > array[j+1]
            swap array[j] and array[j+1]
            swapped = true
    if swapped == false
        break
```

---

**Why Best Case is Linear (O(n))**

-In the best case, the array is already sorted.
-The algorithm does not know this in advance, but the swapped flag detects it during the first pass.
-Since no swaps occur, the loop breaks after the first pass.
-Only n-1 comparisons are made → O(n).       

---

**Time Complexity:**

-Best Case: O(n) → The array is already sorted. Only one pass is needed to confirm the order.
-Average Case: O(n²) → Randomly ordered array; multiple passes and swaps required.
-Worst Case: O(n²) → Array is sorted in reverse; maximum number of comparisons and swaps.

**Space Complexity:**

O(1) → Bubble Sort sorts the array in place, so no extra memory is needed.