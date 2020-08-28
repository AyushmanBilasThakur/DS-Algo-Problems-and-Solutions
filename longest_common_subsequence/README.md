[Go back to listing](../README.md)

# Problem Name - Longest Common Subsequence

**Problem Statement:** Given two strings, find the length of Longest Common Sub Sequence. 

**Input Formatting:** 

```
input_string_1
input_string_2
```

output format:

```
number 
```

**Example Cases:**

    Case 1 - Input Sting 1: "" Input Sting 2: "a" Output: 0
    Case 2 - Input Sting 1: "awwa" Input Sting 2: "awa" Output: 3(awa)
    Case 2 - Input Sting 1: "adtat" Input Sting 2: "awataat" Output: 3(atat)

## How to solve:

(Let's assume the lenght of two stings are n each)

1. **Brute Force Approach:**

Checking all the possible subsequences. 

Time taken: O((2^n) * n) [2^n to trial for all the possible subsequence and n to check that with other string]

2. **Dynamic Programming Approach:(Optimal Solution)**

We are memorizing results from previous smaller substring and filling up a 2D array

Time taken: O(n*n) 

## Points to note

1. **SubString vs Subsequence:** SubSting is a continuous part of a string, where as SubSequence is a part of sting. It can be continuous or it can not be as well.  