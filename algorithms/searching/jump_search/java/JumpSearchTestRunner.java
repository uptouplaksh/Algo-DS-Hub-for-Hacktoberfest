/**
 * Simple Test Runner for JumpSearch (without JUnit dependencies)
 * This ensures tests can be verified without requiring JUnit installation
 */
public class JumpSearchTestRunner {
    
    private static int testsPassed = 0;
    private static int testsFailed = 0;
    
    public static void main(String[] args) {
        System.out.println("╔════════════════════════════════════════════════════════════════╗");
        System.out.println("║          JUMP SEARCH TEST VERIFICATION                         ║");
        System.out.println("╚════════════════════════════════════════════════════════════════╝\n");
        
        testElementPresent();
        testElementNotPresent();
        testFirstElement();
        testLastElement();
        testEmptyArray();
        testSingleElementArray();
        
        System.out.println("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
        System.out.println("RESULTS: " + testsPassed + "/" + (testsPassed + testsFailed) + " tests PASSED");
        System.out.println("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
        
        if (testsFailed == 0) {
            System.out.println("✅ All tests PASSED!");
        } else {
            System.out.println("❌ Some tests FAILED!");
            System.exit(1);
        }
    }
    
    public static void testElementPresent() {
        int[] arr = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
        int target = 13;
        int expected = 6;
        int result = JumpSearch.jumpSearch(arr, target);
        
        if (result == expected) {
            System.out.println("✅ testElementPresent PASSED");
            testsPassed++;
        } else {
            System.out.println("❌ testElementPresent FAILED (expected: " + expected + ", got: " + result + ")");
            testsFailed++;
        }
    }
    
    public static void testElementNotPresent() {
        int[] arr = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
        int target = 8;
        int expected = -1;
        int result = JumpSearch.jumpSearch(arr, target);
        
        if (result == expected) {
            System.out.println("✅ testElementNotPresent PASSED");
            testsPassed++;
        } else {
            System.out.println("❌ testElementNotPresent FAILED (expected: " + expected + ", got: " + result + ")");
            testsFailed++;
        }
    }
    
    public static void testFirstElement() {
        int[] arr = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
        int target = 2;
        int expected = 0;
        int result = JumpSearch.jumpSearch(arr, target);
        
        if (result == expected) {
            System.out.println("✅ testFirstElement PASSED");
            testsPassed++;
        } else {
            System.out.println("❌ testFirstElement FAILED (expected: " + expected + ", got: " + result + ")");
            testsFailed++;
        }
    }
    
    public static void testLastElement() {
        int[] arr = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
        int target = 20;
        int expected = 9;
        int result = JumpSearch.jumpSearch(arr, target);
        
        if (result == expected) {
            System.out.println("✅ testLastElement PASSED");
            testsPassed++;
        } else {
            System.out.println("❌ testLastElement FAILED (expected: " + expected + ", got: " + result + ")");
            testsFailed++;
        }
    }
    
    public static void testEmptyArray() {
        int[] arr = {};
        int target = 5;
        int expected = -1;
        int result = JumpSearch.jumpSearch(arr, target);
        
        if (result == expected) {
            System.out.println("✅ testEmptyArray PASSED");
            testsPassed++;
        } else {
            System.out.println("❌ testEmptyArray FAILED (expected: " + expected + ", got: " + result + ")");
            testsFailed++;
        }
    }
    
    public static void testSingleElementArray() {
        int[] arr = {42};
        boolean passed = true;
        
        // Test for element found
        int result1 = JumpSearch.jumpSearch(arr, 42);
        if (result1 != 0) {
            System.out.println("❌ testSingleElementArray FAILED (finding 42: expected 0, got: " + result1 + ")");
            passed = false;
        }
        
        // Test for element not found
        int result2 = JumpSearch.jumpSearch(arr, 10);
        if (result2 != -1) {
            System.out.println("❌ testSingleElementArray FAILED (finding 10: expected -1, got: " + result2 + ")");
            passed = false;
        }
        
        if (passed) {
            System.out.println("✅ testSingleElementArray PASSED");
            testsPassed++;
        } else {
            testsFailed++;
        }
    }
}
