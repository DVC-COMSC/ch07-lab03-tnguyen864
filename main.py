# List for 5 int values
numbers = []

# List for values > avg of numbers
greater = []

# Get 5 int values and add to list
print("Enter 5 integer values: ")
for i in range(5):
    numbers.append(int(input()))

# Get avg of list sum
avg = sum(numbers) // 5

# Find elements in list > avg
for i in range(5):
    if numbers[i] > avg:
        great = numbers[i]
        greater.append(great)

# Print numbers/greater list
print("List:", end = ' ')
for i in range(5):
    print(numbers[i], end = ' ')
print("\nAverage of list:", avg)

print("Greater than average:", end = ' ')
j = 0
for j in range(2):
    print(greater[j], end = ' ')