[Go back to listing](../README.md)

# Problem Name - Lucky Number Problem

**Problem Statement:** Someone makes lucky number just consisting of 4s and 7s. You need to find the minimum lucky number making the sum N.

**Constrains given:** 0<= N <= 10^6

**Input Formatting:** 

```
N
```

output format:

```
the number consisting 4 and 7 And -1 if impossible
```

**Example Cases:**

    Case 1 - Input: 14 Output: 77
    Case 2 - Input: 32 Output: 47777. [Point to note: 8 4's can also make 32. But we need the smallest number]

## How to solve:

Immmidiately looking at the constraint of N we can conclude that this problem needs to be solved at O(NlogN) time complexity.

So my approcah will be looking at How many total 4's are needed to reach the sum and total number of 7's needed to reach the sum. Then we will start with half the number of 4's and 7's together and adjust step by step. As it is taking the divide and conqure approach, so it is bound to solve the problem in NlogN.


## Points to know: 

If the bound is 10^6 it is typically a O(NlogN) complexity problem and NlogN problems are generally approachable by divide and conqure.