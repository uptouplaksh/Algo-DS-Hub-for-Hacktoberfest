/*
* Program to calculate GCD(HCF) of two positive integers using Euclidean Algorithm
* Time complexity: O(log(min(a,b)))
* Space complexity: O(log(min(a,b))) due to recursion stack, O(1) in interative approach
*/
#include <iostream>
#include <algorithm>
using namespace std;
/*import necessary libraries
iostream for input/output operations
algorithm for using max and min functions*/

//GCD calculation function
int gcd(int a, int b) {
    //Calculate GCD using recursive Euclidean algorithm
    if(a<0 || b<0){
        cout<< "GCD is not defined for negative integers." << endl;
        return -1; //return -1 for invalid input
    }
    if (b == 0)
        return a; //return when base case is true
    return gcd(b, a % b); //recursive call
}

//Iterative version of GCD calculation 
int gcd_iterative(int a,int b){ 
    //Calculate GCD using iterative Euclidean algorithm
    if(a<0 || b<0){
        cout<< "GCD is not defined for negative integers." << endl;
        return -1; //return -1 for invalid input
    }
    while(b != 0){
        int temp = b; //store b in a temporary variable
        b = a % b; //update b to a mod b
        a = temp; //update a to the old value of b
    }
    return a; //return GCD when b becomes 0
}

int main(){
    cout << "GCD of 16 and 12 is " << gcd(max(12,16), min(12,16)) << endl; //output the GCD by calling the gcd function
    cout << "GCD of 54 and 24 is " << gcd_iterative(max(54,24), min(54,24)) << endl; //output the GCD by calling the iterative gcd function
    //use max and min to ensure correct order for gcd function

    return 0;
}

/*
* Sample Output: 
*  GCD of 16 and 12 is 4
*  GCD of 54 and 24 is 6
*
*/