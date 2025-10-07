# Bubble Sort

## 🔹 What is Bubble Sort?
Bubble Sort is a simple sorting algorithm that repeatedly compares **adjacent elements** in an array and **swaps them** if they are in the wrong order.  
This process continues until the entire array is sorted. The largest values "bubble up" to the end of the array, similar to bubbles rising in water.

---

## 🔹 Step-by-Step Example

We want to sort the array: `[5, 1, 4, 2, 8]`

### **Pass 1:**
1. Compare 5 and 1 → swap → `[1, 5, 4, 2, 8]`
2. Compare 5 and 4 → swap → `[1, 4, 5, 2, 8]`
3. Compare 5 and 2 → swap → `[1, 4, 2, 5, 8]`
4. Compare 5 and 8 → no swap → `[1, 4, 2, 5, 8]`

### **Pass 2:**
1. Compare 1 and 4 → no swap → `[1, 4, 2, 5, 8]`
2. Compare 4 and 2 → swap → `[1, 2, 4, 5, 8]`
3. Compare 4 and 5 → no swap → `[1, 2, 4, 5, 8]`
4. Compare 5 and 8 → no swap → `[1, 2, 4, 5, 8]`

✅ The array is now sorted.

---

## 🔹 Time and Space Complexity

**Time Complexity:**

Best Case: O(n) → The array is already sorted. Only one pass is needed to confirm the order.

Average Case: O(n²) → Randomly ordered array; multiple passes and swaps required.

Worst Case: O(n²) → Array is sorted in reverse; maximum number of comparisons and swaps.

**Space Complexity:**

O(1) → Bubble Sort sorts the array in place, so no extra memory is needed.




