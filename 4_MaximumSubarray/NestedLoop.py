list_numbers = [1, 2, 3, 4, 5]

for length in range(1, len(list_numbers) + 1):
    result = []
    for i in range(len(list_numbers) - length + 1):
        print("i =", i)
        result.extend(list_numbers[i:i+length])
    print(result)

# Calculate the sum of the original list
total_sum = sum(list_numbers)
print("Sum of the original list:", total_sum)
