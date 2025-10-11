/**
 * Unit Tests for Coin Change Algorithm
 * 
 * This file contains test cases to verify the correctness of the coinChange function.
 * Tests use console.assert() for simple, dependency-free testing.
 * 
 * To run: node TestCoinChange.js
 */

// Import the coinChange function
// Assuming CoinChange.js exports the function or we include it here
function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;

  for (let i = 1; i <= amount; i++) {
    for (const coin of coins) {
      if (i - coin >= 0) {
        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
      }
    }
  }

  return dp[amount] === Infinity ? -1 : dp[amount];
}

// Test counter
let testsPassed = 0;
let testsTotal = 0;

/**
 * Helper function to run a test
 */
function test(description, fn) {
  testsTotal++;
  try {
    fn();
    testsPassed++;
    console.log(`✓ ${description}`);
  } catch (error) {
    console.error(`✗ ${description}`);
    console.error(`  ${error.message}`);
  }
}

// -------------------------------------------------------------
// Test Cases
// -------------------------------------------------------------

console.log('\n🧪 Running Coin Change Tests...\n');

// Test 1: Standard case - amount = 11, coins = [1, 2, 5]
test('Standard case: amount=11, coins=[1,2,5] should return 3', () => {
  const result = coinChange([1, 2, 5], 11);
  console.assert(result === 3, `Expected 3, but got ${result}`);
});

// Test 2: Impossible case - amount cannot be made
test('Impossible case: amount=3, coins=[2] should return -1', () => {
  const result = coinChange([2], 3);
  console.assert(result === -1, `Expected -1, but got ${result}`);
});

// Test 3: Base case - amount = 0
test('Base case: amount=0 should return 0', () => {
  const result = coinChange([1, 2, 5], 0);
  console.assert(result === 0, `Expected 0, but got ${result}`);
});

// Test 4: Single coin needed
test('Single coin: amount=5, coins=[5] should return 1', () => {
  const result = coinChange([5], 5);
  console.assert(result === 1, `Expected 1, but got ${result}`);
});

// Test 5: Multiple coins of same denomination
test('Multiple same coins: amount=6, coins=[2] should return 3', () => {
  const result = coinChange([2], 6);
  console.assert(result === 3, `Expected 3, but got ${result}`);
});

// Test 6: Large denomination with smaller ones
test('Mixed denominations: amount=30, coins=[1,5,10,25] should return 2', () => {
  const result = coinChange([1, 5, 10, 25], 30);
  console.assert(result === 2, `Expected 2, but got ${result}`);
});

// Test 7: No coins available
test('Empty coins array: amount=5, coins=[] should return -1', () => {
  const result = coinChange([], 5);
  console.assert(result === -1, `Expected -1, but got ${result}`);
});

// Test 8: Amount less than smallest coin
test('Amount smaller than coins: amount=1, coins=[2,5,10] should return -1', () => {
  const result = coinChange([2, 5, 10], 1);
  console.assert(result === -1, `Expected -1, but got ${result}`);
});

// Test 9: Greedy approach would fail
test('Non-greedy case: amount=6, coins=[1,3,4] should return 2', () => {
  const result = coinChange([1, 3, 4], 6);
  console.assert(result === 2, `Expected 2 (3+3), but got ${result}`);
});

// Test 10: Larger amount
test('Larger amount: amount=100, coins=[1,5,10,25] should return 4', () => {
  const result = coinChange([1, 5, 10, 25], 100);
  console.assert(result === 4, `Expected 4 (25+25+25+25), but got ${result}`);
});

// -------------------------------------------------------------
// Test Summary
// -------------------------------------------------------------
console.log(`\n${'='.repeat(50)}`);
console.log(`📊 Test Results: ${testsPassed}/${testsTotal} tests passed`);
if (testsPassed === testsTotal) {
  console.log('✅ All tests passed!');
} else {
  console.log(`❌ ${testsTotal - testsPassed} test(s) failed`);
}
console.log(`${'='.repeat(50)}\n`);
