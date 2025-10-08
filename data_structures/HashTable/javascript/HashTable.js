/*
HashTable Implementation in JavaScript with Chaining for collision handling.
Time Complexity:
set(key, value): Average O(1), Worst O(n)
get(key): Average O(1), Worst O(n)
remove(key): Average O(1), Worst O(n)
(Worst case occurs when all keys hash to the same bucket, degrading to a linear search)
Space Complexity: O(n), where n is the number of key-value pairs stored.
*/

// HashTable implementation in JavaScript using chaining for collision handling

class HashTable {
  constructor(size = 42) {
    // Initialize hash table size and create buckets (arrays) for chaining
    this.size = size;
    this.buckets = new Array(size).fill(null).map(() => []);
  }

  // Simple hash function to convert a key string into an index
  _hash(key) {
    let hash = 0;
    for (let char of key) {
      hash += char.charCodeAt(0);
    }
    return hash % this.size;
  }

  // Set a key-value pair in the hash table
  set(key, value) {
    const index = this._hash(key);
    const bucket = this.buckets[index];

    // Check if key already exists, update value if found
    for (let pair of bucket) {
      if (pair[0] === key) {
        pair[1] = value;
        return;
      }
    }

    // If key does not exist, add new key-value pair
    bucket.push([key, value]);
  }

  // Get the value associated with a key
  get(key) {
    const index = this._hash(key);
    const bucket = this.buckets[index];

    for (let pair of bucket) {
      if (pair[0] === key) {
        return pair[1];
      }
    }

    // Return undefined if key is not found
    return undefined;
  }

  // Remove a key-value pair by key
  remove(key) {
    const index = this._hash(key);
    const bucket = this.buckets[index];

    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        bucket.splice(i, 1);
        return true; // Removal successful
      }
    }

    return false; // Key not found
  }
}

// Runnable example to test the HashTable class
const ht = new HashTable();

// Add some key-value pairs
ht.set('name', 'MCA Student');
ht.set('course', 'Web Development');
ht.set('location', 'Pune');

// Retrieve and log values
console.log('Name:', ht.get('name'));           // Expected: MCA Student
console.log('Course:', ht.get('course'));       // Expected: Web Development
console.log('Location:', ht.get('location'));   // Expected: Pune

// Update location value
ht.set('location', 'Mumbai');
console.log('Updated Location:', ht.get('location')); // Expected: Mumbai

// Remove the course key-value pair
ht.remove('course');
console.log('Course after removal:', ht.get('course')); // Expected: undefined

// Try removing a key that doesn't exist
console.log('Remove course again:', ht.remove('course')); // Expected: false

// Add a key that causes collision but update value
ht.set('name', 'New Name');
console.log('Updated Name:', ht.get('name')); // Expected: New Name
