# Taking input
arr_length = int(input())
arr_string = input()
arr = [int(i) for i in arr_string.split(" ")]

# Solving for the sum
current_sum = arr[0]
highest_sum = arr[0]

for i in range(1, arr_length):
    current_sum = max(current_sum + arr[i], arr[i])
    highest_sum = max(current_sum, highest_sum)


# Solving for sum and index
current_sum = arr[0]
current_start = 0
highest_sum = arr[0]
highest_start = 0
highest_end = 0

for i in range(1, arr_length):
    current_sum = current_sum + arr[i]
    if(arr[i] > current_sum):
        current_start = i
        current_sum = arr[i]
    
    if(current_sum > highest_sum):
        highest_sum = current_sum
        highest_start = current_start
        highest_end = i


print(highest_start, highest_end, highest_sum)