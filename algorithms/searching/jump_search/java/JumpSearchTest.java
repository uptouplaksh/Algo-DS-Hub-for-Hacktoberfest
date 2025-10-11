import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Unit tests for Jump Search Algorithm
 * 
 * This class contains comprehensive unit tests for the jumpSearch method
 * to verify its correctness against various edge cases.
 */
public class JumpSearchTest {

    /**
     * Test for an element present in the array.
     */
    @Test
    public void testElementPresent() {
        int[] arr = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
        int target = 13;
        int result = JumpSearch.jumpSearch(arr, target);
        assertEquals(6, result, "Element 13 should be found at index 6");
    }

    /**
     * Test for an element not present in the array.
     */
    @Test
    public void testElementNotPresent() {
        int[] arr = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
        int target = 8;
        int result = JumpSearch.jumpSearch(arr, target);
        assertEquals(-1, result, "Element 8 should not be found, return -1");
    }

    /**
     * Test for the first element in the array.
     */
    @Test
    public void testFirstElement() {
        int[] arr = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
        int target = 2;
        int result = JumpSearch.jumpSearch(arr, target);
        assertEquals(0, result, "First element should be found at index 0");
    }

    /**
     * Test for the last element in the array.
     */
    @Test
    public void testLastElement() {
        int[] arr = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
        int target = 20;
        int result = JumpSearch.jumpSearch(arr, target);
        assertEquals(9, result, "Last element should be found at index 9");
    }
}
