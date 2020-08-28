def max(a, b):
    if(a > b): 
        return a
    else:
        return b 

a = input()
b = input()

len_a = len(a)
len_b = len(b)

# print(a[1],b[1],len(a), len(b))

solution_table = [[0]*(len_b + 1)]*(len_a + 1)

for i in range(0, len_a + 1):
    for j in range(0, len_b + 1):
        if i == 0 or j == 0:
            continue
        elif a[i-1] == b[j-1]:
            solution_table[i][j] = solution_table[i-1][j-1] + 1
        else:
            solution_table[i][j] = max(solution_table[i-1][j], solution_table[i][j-1])

print(solution_table[len_a][len_b])