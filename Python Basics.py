# Question 4: Write a Python program to take a user's name as input and print a greeting message.

name = input("Enter your name: ")

print(f"Hello, {name}! Welcome to the world of Python.")

# Question 5: Write a Python program to check whether a number is even or odd using conditional statements.


number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")

# Question 6: Write a program to print numbers from 1 to 10 using a loop.

for i in range(1, 11):
    print(i)


# Question 7: Create a list of five numbers and print the maximum number from the list.


numbers = [14, 45, 8, 92, 23]

max_num = max(numbers)
print("The maximum number in the list is:", max_num)

# Question 8: Write a Python program to remove duplicate values from a list using a set.

original_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_list = list(set(original_list))

print("Original List:", original_list)
print("List after removing duplicates:", unique_list)

# Question 9: Write a function that returns the square of a number.

def square_number(num):
    return num ** 2
n
result = square_number(5)
print("The square of 5 is:", result)



# Question 10: Write a Python program to count how many times a number appears in a list.

example_list = [2, 3, 4, 2, 5, 2]
target_number = 2
count_occurrence = example_list.count(target_number)

print(f"The number {target_number} appears {count_occurrence} times in the list.")