/* C++ program to implement fractional knapsack problem using greedy method
* Objective of the knapsack problem is to obtain a filling of the knapsack of given size that maximizes the total profit earned.
* Time complexity: O(n log n) due to sorting, O(n) for knapsack filling
* Space complexity: O(n) for storing weights and profits
*/

#include <bits/stdc++.h>
using namespace std;
class knapsack{
    private:
    int m,n; //m is the maximum capacity of knapsack, n is the number of items
    vector<float> p; //p is the profits array
    vector<float> w; //w is the weights array
   public:
   // Constructor to initialize the knapsack object with given parameters
   knapsack(int knapsack_size, vector<float> profits, vector<float> weights) {
    m = knapsack_size;  // Store the maximum capacity of the knapsack
    p = profits;        // Store the profits array for each item
    w = weights;        // Store the weights array for each item
    n = p.size();       // Store the total number of items (derived from profits array size)
    }
 
     // Merge function to combine two sorted subarrays based on profit-to-weight ratio
     void merge(int left, int mid, int right) {
        int n1 = mid - left + 1;    // Size of left subarray
        int n2 = right - mid;       // Size of right subarray

        // Create temporary arrays to store left and right subarrays
        vector<float> Lp(n1), Lw(n1), Rp(n2), Rw(n2);
        
        // Copy data from original arrays to left temporary arrays
        for (int i = 0; i < n1; i++) {
            Lp[i] = p[left + i];     // Copy profits of left subarray
            Lw[i] = w[left + i];     // Copy weights of left subarray
        }
        // Copy data from original arrays to right temporary arrays
        for (int j = 0; j < n2; j++) {
            Rp[j] = p[mid + 1 + j];  // Copy profits of right subarray
            Rw[j] = w[mid + 1 + j];  // Copy weights of right subarray
        }

        // Initialize indices for merging
        int i = 0, j = 0, k = left;  // i for left array, j for right array, k for merged array
        
        // Merge the two subarrays in descending order of profit-to-weight ratio
        while (i < n1 && j < n2) {
            float r1 = Lp[i] / Lw[i];   // Calculate profit-to-weight ratio for left element
            float r2 = Rp[j] / Rw[j];   // Calculate profit-to-weight ratio for right element
            
            // Choose element with higher profit-to-weight ratio (greedy choice)
            if (r1 >= r2) {
                p[k] = Lp[i];           // Place left element in merged array
                w[k] = Lw[i];
                i++;                    // Move to next element in left subarray
            } else {
                p[k] = Rp[j];           // Place right element in merged array
                w[k] = Rw[j];
                j++;                    // Move to next element in right subarray
            }
            k++;                        // Move to next position in merged array
        }

        // Copy remaining elements from left subarray (if any)
        while (i < n1) {
            p[k] = Lp[i];
            w[k] = Lw[i];
            i++; k++;
        }
        
        // Copy remaining elements from right subarray (if any)
        while (j < n2) {
            p[k] = Rp[j];
            w[k] = Rw[j];
            j++; k++;
        }
    }

    // Recursive merge sort function to sort items by profit-to-weight ratio
    void mergeSort(int left, int right) {
        if (left < right) {                    // Base case: if left < right, continue sorting
            int mid = (left + right) / 2;      // Find the middle point to divide array
            
            mergeSort(left, mid);              // Recursively sort first half
            mergeSort(mid + 1, right);         // Recursively sort second half
            
            merge(left, mid, right);           // Merge the two sorted halves
        }
    }
    
    // Public function to initiate sorting of all items by profit-to-weight ratio
    void sortItems(){
       mergeSort(0, n-1);                     // Sort entire array from index 0 to n-1
    }
   vector<float> frac_knap (){ //knapsack function
    vector<float> x(n,0);
    int i,u=m;
    for(i=0;i<n;i++){ //loop through all items
        if(w[i]>u) break; //if weight of item is greater than remaining capacity, break
        else{
        x[i]=1.0; //else add whole item
        u-=w[i];
        } //reduce remaining capacity
    }
    if(i<=n){ //if there are still items left
        x[i]=u/w[i]; //add fraction of the next item
    }
    
    return x;//return the vector containing fractions of items added to knapsack
   }
   int calc_profit(vector<float> x){ //calculate profit from the fractions of items added to knapsack
    int profit=0;
    for(int i=0;i<n;i++){
        profit+=x[i]*p[i]; //multiply fraction of item by its profit and add to total profit
    }
    return profit; //return total profit
   }

};
int main(){ //main function
    int knapsack_size=5, total_items=3;//default values
    vector<float> profits={700,500,900};//default values
    vector<float> weights={7,1,3};//default values
    knapsack k(knapsack_size, profits, weights); //create knapsack class object
     //take input
    k.sortItems(); //sort items according to profit/weight ratio
   vector<float> x =k.frac_knap(); //call knapsack function to get fractions of items added to knapsack
    cout<<"Knapsack is\n"; 
    for(float a:x){
        cout<<a<<" "; //print fractions of items added to knapsack
    }  
    cout<<endl;
    cout<<"Profit is "<<k.calc_profit(x)<<endl; //calculate and print total profit
    return 0;
}
/*
* Sample Input/Output:
*Knapsack is
* 1 1 0.142857 
* Profit is 1500
*/
