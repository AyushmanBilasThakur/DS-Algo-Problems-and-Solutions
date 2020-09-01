[Go back to listing](../README.md)

# Problem Name - Maximum Contiguous Subarray

**Problem Statement:** Given an array of integers find out the starting and ending index of the subarray that gives the maximum sum 

**Input Formatting:** 

```
number of elements in the array
elemnts sepereaterd by space
```

output format:

```
number,number(if seeking the range)
number(if seeking the sum)
```

**Example Cases:**

    Case 1 - Input Array: [1 2 3 4 5] Output: 0,5[If seeking the sum return 15]
    Case 2 - Input Array: [-1 -2 -3 -4 -5] Output: 0,0[If seeking sum return -1]
    Case 2 - Input Array: [-1 -5 3 4 -2] Output: 2,3[If seeking the sum return 7]

## How to solve:

(Let's assume the lenght of the array n)

1. **Brute Force Approach:**

Checking all the possible subarrays. 

Time taken: O((2^n)) [2^n to trial for all the possible subarray]

2. **Dynamic Programming Approach:**

We are memorizing results from previous smaller subarray and filling up a 2D array

Time taken: O(n*n) 

3. **Kaden's Algorithm:**

We go through the array only once, going on calculating the sum

Time complexity: O(n)