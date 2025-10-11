

#include <stdio.h>
#include <math.h>  // Include math library for pow() function

/**
 * Function to check if a number is an Armstrong number
 * @param num: The number to check
 * @return: 1 if Armstrong number, 0 otherwise
 */
int isArmstrongNumber(int num) {
    int originalNum = num;
    int temp = num;
    int digitCount = 0;
    int result = 0;
    int remainder;
    
    // Handle special case of 0
    if (num == 0) return 1;
    
    //digit counter
    while (temp != 0) {
        digitCount++;
        temp /= 10;
    }
    
    // savind original number
    temp = originalNum;
    
    // Calculate sum of each digit raised to power of digit count
    while (temp != 0) {
        remainder = temp % 10;  // Extract last digits
        result += pow(remainder, digitCount);  // Add digit^digitCount to result
        temp /= 10;  // extracting left over number
    }
    
    // Return 1 if Armstrong number, 0 otherwise
    return (result == originalNum);
}

// Main function
int main() {
    int userNumber;
    
    printf("Enter a number to check: ");
    scanf("%d", &userNumber);
    
    if (isArmstrongNumber(userNumber)) {
        printf("%d is an Armstrong number.\n", userNumber);
    } else {
        printf("%d is not an Armstrong number.\n", userNumber);
    }
    
    return 0;
}