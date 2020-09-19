visited = []
N = int(input())

def approach_n(curr):

    for e in visited: 
        if e == curr:
            return -1

    visited.append(curr)

    sum = curr[0] * 4 + curr[1] * 7
    if sum == N:
        return curr

    approach_a = []
    approach_b = []

    if(sum > N):
        if(curr[0] - 1 < 0 or curr[1] - 1 < 0):
            return -1
        approach_a = approach_n([curr[0] - 1, curr[1]])
        approach_b = approach_n([curr[0], curr[1] - 1])
    else:
        if(curr[0] + 1 > N // 4 or curr[1] + 1 > N // 7):
            return -1
        approach_a = approach_n([curr[0] + 1, curr[1]])
        approach_b = approach_n([curr[0], curr[1] + 1])

    # print(approach_a, approach_b)

    if(approach_a == -1 and approach_b == -1):
        return -1

    elif(approach_a == -1):
        return approach_b

    elif(approach_b == -1):
        return approach_a

    else:
        if(approach_a[0] + approach_a[1] > approach_b[0] + approach_b[1]):
            return(approach_b)
        else:
            return(approach_a)



max_four = N // 4
max_seven = N // 7

res = approach_n([max_four, max_seven])

if res == -1:
    print(-1)

else: 
    x = ""
    for i in range(0, res[0]):
        x += "4"
    for i in range(0, res[1]):
        x += "7"

    print(x)