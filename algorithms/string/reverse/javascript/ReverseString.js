/**
 * Reverses a given string without using the built-in .reverse() method.
 *
 * @param {string} str The string to be reversed.
 * @returns {string} The reversed string.
 */
function reverseString(str) {
  let reversed = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  return reversed;
}

/**
 * Complexity Analysis:
 * Time Complexity: O(n) - We loop through the string once.
 * Space Complexity: O(n) - We create a new string to store the reversed version.
 * where n is the length of the input string.
 */

/**
 * Runnable Example:
 */
const originalString = "Hello, World!";
const reversedStr = reverseString(originalString);
console.log(`Original: "${originalString}"`);
console.log(`Reversed: "${reversedStr}"`); // Expected output: "!dlroW ,olleH"
