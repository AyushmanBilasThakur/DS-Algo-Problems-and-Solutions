#include<bits/stdc++.h>

using namespace std;

int main(){
    //variables for temporary storage and loops
    int i,t = 0;

    //Taking user input
    int arr_length;
    vector<int> arr;
    cin>>arr_length;
    for(i = 0; i < arr_length; i++){
        cin>>t;
        arr.push_back(t);
    } 

    cout<<endl;

    //looking through the array
    int current_sum = arr[0], total_highest_sum = arr[0];

    // if you just need to find the highst continuos sum
    
    /*
    for(i = 1; i < arr_length; i++){
        // common debugging line 1
        // cout<<i<<" - "<<arr[i]<<" "<<current_sum<<" "<<total_highest_sum<<endl;
        current_sum += arr[i];
        current_sum = max(current_sum, arr[i]);
        total_highest_sum = max(total_highest_sum, current_sum);
    }
    */

    // if you need the indexes
    int current_starting_index = 0, global_starting_index = 0, global_ending_index = 0;

    for(i = 1; i < arr_length; i++){
        current_sum += arr[i];
        if(arr[i] > current_sum){
            current_sum = arr[i];
            current_starting_index = i;
        }

        if(current_sum > total_highest_sum){
            total_highest_sum = current_sum;
            global_starting_index = current_starting_index;
            global_ending_index = i;
        }
    }

    cout << global_starting_index << "," << global_ending_index << " - " << total_highest_sum << endl;

    return 0;
}