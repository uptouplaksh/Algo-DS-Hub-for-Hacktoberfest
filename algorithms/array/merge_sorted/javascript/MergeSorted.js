/*
Merge Two Sorted Arrays in JavaScript

Time Complexity:
- O(n + m) where n and m are lengths of the two arrays.

Space Complexity:
- O(n + m) for the output array.

Description:
This function takes two sorted arrays and merges them into a single sorted array.
It iterates through both arrays, comparing elements, and pushes the smaller element
into the result array. Once one array is exhausted, the remaining elements from the
other array are appended.
*/

function mergeSortedArrays(arr1, arr2) {
    let merged = []; // Result array
    let i = 0; // Pointer for arr1
    let j = 0; // Pointer for arr2

    // Traverse both arrays and push smaller element into merged
    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] <= arr2[j]) {
            merged.push(arr1[i]);
            i++;
        } else {
            merged.push(arr2[j]);
            j++;
        }
    }

    // Append remaining elements from arr1
    while (i < arr1.length) {
        merged.push(arr1[i]);
        i++;
    }

    // Append remaining elements from arr2
    while (j < arr2.length) {
        merged.push(arr2[j]);
        j++;
    }

    return merged;
}

/* Example Usage */
const array1 = [1, 3, 5, 7];
const array2 = [2, 4, 6, 8];

const mergedArray = mergeSortedArrays(array1, array2);
console.log("Merged Array:", mergedArray);
// Output: Merged Array: [1, 2, 3, 4, 5, 6, 7, 8]
